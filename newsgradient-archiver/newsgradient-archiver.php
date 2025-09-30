<?php

/*
* Plugin Name: Newsgradient Archiver
* Plugin URI: https://newsgradient-pwa.lb.djnd.si/plugin
* Description: Automatically archives all URLs when saving a post.
* Version: 0.0.4
* Requires at least: 5.2
* Requires PHP: 7.2
* Author: Danes je nov dan
* Author URI: https://danesjenovdan.si
* License: The Unlicense
* License URI: https://unlicense.org/
* Update URI: https://newsgradient-pwa.lb.djnd.si/plugin
* Text Domain: newsgradient-archiver
* Domain Path: /archiver
*/


function archive_url($url)
{
    $api_key = get_option('ng_archiver_wayback_api_key');
    $api_url = 'https://web.archive.org/save/' . $url;

    $response = wp_safe_remote_get($api_url, array(
        'headers' => array(
            'Accept' => 'application/json',
            'Authorization' => 'LOW ' . $api_key,
        ),
    ));

    if (!is_wp_error($response)) {
        // Return the archived URL
        return 'https://web.archive.org/web/' . $url;
    }

    // Return the original URL if archiving fails
    return $url;
}

function replace_urls_with_archived($content)
{
    if ($content !== '') {
        // try with DOMDocument
        $dom = new DOMDocument();
        // make sure UTF-8 doesn't break things
        $better_content = mb_convert_encoding($content, 'HTML-ENTITIES', "UTF-8");
        // make it a full HTML document
        $dom->loadHTML('<!DOCTYPE html><body>' . $better_content . '</body></html>');

        // find all anchor tags, then iterate through them
        $anchors = $dom->getElementsByTagName('a');
        foreach ($anchors as $element) {
            $original_href = $element->getAttribute('href');
            // if not already archived (check if href begins with the archiving base url), archive the url
            if (strpos($original_href, 'https://web.archive.org') !== 0) {
                $element->setAttribute('href', archive_url($original_href));
            }
        }

        // the transformation is done, time to render the new post content
        // xpath is for querying the DOM
        $xpath = new DOMXPath($dom);
        // query the whole body
        $body = $xpath->query('/html/body')->item(0);
        // transform the body to string
        $body_string = $dom->saveHTML($body);
        // remove <body> and </body> from the rendered string
        $clean_body = substr($body_string, 6, -7);

        // // old pattern was too greedy
        // // $pattern = '/href=["\']?(https?:\/\/[^\s]+)/';
        // $pattern = '/href=["\']?(https?:\/\/[a-z0-9+!*\(\),;?&=\$_.-]+)["\']?/';
        // preg_match_all($pattern, $content, $matches);

        // $handled_urls = [];

        // foreach ($matches[1] as $url) {
        //     if (!in_array($url, $handled_urls)) {
        //         array_push($handled_urls, $url);
        //         $archived_url = archive_url($url);
        //         $content = str_replace($url, $archived_url, $content);
        //     }
        // }

        return $clean_body;
    }
    return $content;
}

function save_archived_version($post_id, $post, $update)
{
    // unhook this function so it doesn't loop infinitely
    remove_action('save_post', 'save_archived_version');

    // update the post, which calls save_post again.
    wp_update_post(array('ID' => $post_id, 'post_content' => replace_urls_with_archived($post->post_content)));

    // re-hook this function.
    add_action('save_post', 'save_archived_version');
}

// add_filter('the_content', 'replace_urls_with_archived');
add_action('save_post', 'save_archived_version', 10, 3);

// OPTIONS IN SETTINGS
function ng_archiver_settings_init()
{
    // register a new setting for "writing" page
    register_setting('writing', 'ng_archiver_wayback_api_key');

    // register a new section in the "reading" page
    add_settings_section(
        'ng_archiver_settings_section',
        'Newsgradient Archiver',
        'ng_archiver_settings_section_callback',
        'writing'
    );

    // register a new field in the "ng_archiver_settings_section" section, inside the "writing" page
    add_settings_field(
        'ng_archiver_settings_field',
        'Wayback Machine API key',
        'ng_archiver_settings_field_callback',
        'writing',
        'ng_archiver_settings_section'
    );
}

/**
 * register ng_archiver_settings_init to the admin_init action hook
 */
add_action('admin_init', 'ng_archiver_settings_init');

/**
 * callback functions
 */

// section content cb
function ng_archiver_settings_section_callback()
{
    echo '<p>Please enter your Wayback Machine S3 API key. Get them at <a href="https://archive.org/account/s3.php" target="_blank">https://archive.org/account/s3.php</a>, then paste them into the field below like so:</p><pre>ACCESS_KEY:SECRET_KEY</pre>';
}

// field content cb
function ng_archiver_settings_field_callback()
{
    // get the value of the setting we've registered with register_setting()
    $setting = get_option('ng_archiver_wayback_api_key');
    // output the field
?>
    <input type="text" name="ng_archiver_wayback_api_key" value="<?php echo isset($setting) ? esc_attr($setting) : ''; ?>">
<?php
}

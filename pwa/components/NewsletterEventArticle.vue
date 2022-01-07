<template>
  <div style="border: 1px solid #a8a5a9; background-color: #f6f6f6; margin-top: 15px">
    <a :href="`${article.url}`" style="display: block; text-decoration: none">
      <img :src="`${article.image}`" style="width: 100%; display: block" />
    </a>
    <div style="padding: 15px">
      <div style="margin-bottom: 15px">
        <div style="display: inline-flex; align-items: center">
          <img
            :src="`${faviconIcon(article.url)}`"
            style="display: inline-block; width: 16px; height: 16px; margin: 2.5px 5px 0 0"
          />
          <a
            :href="`${article.url}`"
            style="
              display: inline-block;
              color: #000;
              font-size: 11px;
              font-style: italic;
              line-height: 11px;
              text-decoration: none;
            "
          >
            {{ article.medium__title }}
          </a>
        </div>
        <span
          style="
            float: right;
            background-color: #fff;
            border-radius: 5em;
            padding: 5px 8px;
            font-size: 11px;
            line-height: 1;
          "
        >
          {{ article.social_score }}
          <i
            style="
              display: inline-block;
              width: 12px;
              height: 12px;
              margin: -2px 0 -2px 2px;
              background-image: url('twitter.png');
              background-position: center center;
              background-size: 10px 8px;
              background-repeat: no-repeat;
            "
          ></i>
        </span>
      </div>
      <div>
        <a
          :href="`${article.url}`"
          style="color: #222; font-size: 16px; font-weight: 600; line-height: 1.2; text-decoration: none"
        >
          {{ article.title }}
        </a>
      </div>
      <div style="margin-top: 5px">
        <a
          :href="`${article.url}`"
          style="color: #0177ff; font-size: 11px; line-height: 1.2; text-decoration: underline"
        >
          Pročitaj više
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { faviconIcon } from '../utils'

export default {
  props: {
    article: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {}
  },
  methods: {
    faviconIcon(url) {
      return faviconIcon(url)
    },
  },
}
</script>

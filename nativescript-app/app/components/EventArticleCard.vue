<template>
  <GridLayout
    rows="auto, auto, auto, auto"
    class="event-article-card"
    @loaded="onLoaded"
    @layoutChanged="onLayoutChanged"
  >
    <Image row="0" class="gradient-line" />
    <GridLayout row="1" rows="auto, auto, auto" columns="24, *" class="heading">
      <Image
        row="0"
        col="0"
        :src="faviconUrl"
        stretch="aspectFill"
        class="medium-icon"
      />
      <Label row="0" col="1" :text="article.medium.title" class="medium-name" />
      <StackLayout row="1" col="0" colSpan="2" class="hr" />
      <Label
        row="2"
        col="0"
        colSpan="2"
        :text="article.title"
        textWrap="true"
        class="title"
      />
    </GridLayout>
    <Image ref="image" row="2" :src="article.image" stretch="aspectFill" />
    <GridLayout row="3" rows="auto, auto" class="content">
      <Label
        ref="text"
        row="0"
        :text="articleText"
        textWrap="true"
        class="text"
      />
      <Label row="1" text="Pročitaj više" class="read-more" />
    </GridLayout>
  </GridLayout>
</template>

<script>
export default {
  props: {
    article: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      lastWidth: 0,
    };
  },
  computed: {
    faviconUrl() {
      const { url } = this.article;
      const domain = url.slice(0, url.indexOf('/', url.indexOf('://') + 3));
      return `https://www.google.com/s2/favicons?sz=32&domain_url=${domain}`;
    },
    articleText() {
      const { content } = this.article;
      return content.replace(/\s+/g, ' ').trim();
    },
  },
  methods: {
    onLayoutChanged(arg) {
      const card = arg.object;
      const image = this.$refs.image.nativeView;
      const cardWidth = card.getActualSize().width;
      const imageHeight = this.$refs.image.nativeView.getActualSize().height;
      const newImageHeight = cardWidth * 0.5235; // og image ratio 1:1.91
      if (imageHeight !== newImageHeight) {
        image.height = newImageHeight;
      }
    },
    onLoaded() {
      const maxLines = 3;
      const text = this.$refs.text.nativeView;
      if (text.android) {
        // eslint-disable-next-line no-undef
        const { TruncateAt } = android.text.TextUtils;
        text.android.setEllipsize(TruncateAt.END);
        text.android.setMaxLines(maxLines);
      } else if (text.ios) {
        text.ios.numberOfLines = maxLines;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.event-article-card {
  margin-bottom: 10;
  background-color: #fff;

  .gradient-line {
    height: 2;
    background-image: linear-gradient(to right, #0076fe 0%, #e50001 100%);
  }

  .heading {
    padding: 8;

    .medium-icon {
      horizontal-alignment: left;
      width: 16;
      height: 16;
    }

    .medium-name {
      font-style: italic;
    }

    .hr {
      margin: 8 0;
    }

    .title {
      font-size: 16;
      font-weight: 700;
    }
  }

  .content {
    padding: 8;

    .text {
      font-size: 14;
    }

    .read-more {
      horizontal-alignment: right;
      margin: 8 0 2 0;
      border-radius: 12;
      padding-left: 10;
      padding-right: 25;
      background-color: #0177ff;
      background-image: url('res://arrow');
      background-repeat: no-repeat;
      background-position: right center;
      background-size: 52 25;
      text-transform: uppercase;
    }
  }
}
</style>

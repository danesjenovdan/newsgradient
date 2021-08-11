<template>
  <GridLayout
    rows="auto, auto, auto, auto"
    class="event-article-card"
    @layoutChanged="onLayoutChanged"
    @tap="onTap"
  >
    <StackLayout row="0" class="gradient-line" />
    <GridLayout row="1" rows="auto, auto, auto" columns="24, *" class="heading">
      <NSImg
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
    <NSImg
      ref="image"
      row="2"
      stretch="aspectFill"
      placeholderImageUri="res://logo"
      failureImageUri="res://logo"
      :src="article.image"
    />
    <GridLayout row="3" rows="auto, auto" columns="*, auto" class="content">
      <TruncatedLabel
        row="0"
        col="0"
        colSpan="2"
        :text="articleText"
        :maxLines="3"
        class="text"
      />
      <MoreButton row="1" col="1" text="Pročitaj više" class="read-more" />
    </GridLayout>
  </GridLayout>
</template>

<script>
import { Utils } from '@nativescript/core';
import MoreButton from './MoreButton.vue';
import TruncatedLabel from './TruncatedLabel.vue';

export default {
  components: {
    MoreButton,
    TruncatedLabel,
  },
  props: {
    article: {
      type: Object,
      required: true,
    },
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
      const imageHeight = image.getActualSize().height;
      const newImageHeight = cardWidth * 0.5235; // og image ratio 1:1.91
      if (imageHeight !== newImageHeight) {
        image.height = newImageHeight;
      }
    },
    onTap() {
      if (this.article && this.article.url) {
        Utils.openUrl(this.article.url);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import '@nativescript/theme/scss/variables';

.event-article-card {
  @include colorize($background-color: 'background');

  padding: 0;

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
      padding: 0;
      font-style: italic;
    }

    .hr {
      margin: 8 0 6 0;
    }

    .title {
      padding: 0;
      font-size: 16;
      font-weight: 700;
    }
  }

  .content {
    padding: 6 8 8 8;

    .text {
      padding: 0;
      font-size: 14;
    }

    .read-more {
      margin-top: 6;
    }
  }
}
</style>

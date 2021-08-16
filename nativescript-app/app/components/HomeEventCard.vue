<template>
  <GridLayout columns="auto, *" class="home-event-card" @tap="onTap">
    <GridLayout col="0" class="image-col" :width="imageWidth">
      <NSImg
        stretch="aspectFill"
        placeholderImageUri="res://logo"
        failureImageUri="res://logo"
        :src="event.image"
        :width="imageWidth"
      />
      <StackLayout class="gradient" :width="imageWidth" />
      <GridLayout rows="*, auto" columns="*, auto" class="overlay">
        <SocialScoreBadge row="1" col="1" :text="event.social_score" />
      </GridLayout>
    </GridLayout>
    <GridLayout col="1" rows="auto, auto, *, auto" class="text-col">
      <TruncatedLabel row="0" :text="event.title" :maxLines="3" class="title" />
      <Label row="1" class="date">
        <FormattedString>
          <Span text="Prvi put objavljeno: " fontStyle="italic" />
          <Span :text="event.firstPublish" />
        </FormattedString>
      </Label>
      <GridLayout row="3" columns="auto, *, auto" class="more-row">
        <Label
          col="0"
          :text="`${event.allArticlesCount} ${
            allArticlesCount === 1 ? 'članak' : 'članaka'
          }`"
          class="num-articles"
        />
        <MoreButton col="2" text="Uporedite naslove" />
      </GridLayout>
    </GridLayout>
  </GridLayout>
</template>

<script>
import { Screen } from '@nativescript/core';
import Event from './Event.vue';
import MoreButton from './MoreButton.vue';
import TruncatedLabel from './TruncatedLabel.vue';
import SocialScoreBadge from './SocialScoreBadge.vue';

export default {
  components: {
    MoreButton,
    TruncatedLabel,
    SocialScoreBadge,
  },
  props: {
    event: {
      type: Object,
      required: true,
    },
  },
  data() {
    const isSmallScreen = Screen.mainScreen.widthDIPs <= 360;
    return {
      imageWidth: isSmallScreen ? 100 : 120,
    };
  },
  methods: {
    onTap() {
      this.$navigateTo(Event, {
        transition: {
          name: 'slideLeft',
          duration: 200,
          curve: 'easeInOut',
        },
        props: {
          event: this.event,
        },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import '@nativescript/theme/scss/variables';

.home-event-card {
  @include colorize($background-color: 'background');

  padding: 0;
  height: 120;

  .image-col {
    &,
    .image,
    .gradient {
      // width: 120;
      height: 120;
    }

    .gradient {
      background-image: linear-gradient(to right, #e40001 0%, #4199fe 100%);
      opacity: 0.6;
    }

    .overlay {
      padding: 8;
    }
  }

  .text-col {
    padding: 4 8 8 8;
    height: 120;

    .title {
      padding: 0;
      font-size: 16;
      font-weight: 700;
    }

    .date {
      padding: 0;
      margin-top: 2;
    }

    .more-row {
      .num-articles {
        padding: 5 8 5 0;
        color: #e50001;
      }
    }
  }
}
</style>

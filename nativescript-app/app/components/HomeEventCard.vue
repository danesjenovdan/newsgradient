<template>
  <GridLayout columns="128, *" class="home-event-card" @tap="onTap">
    <GridLayout col="0" class="image-col">
      <Image :src="event.image" stretch="aspectFill" />
      <Image class="gradient" />
    </GridLayout>
    <GridLayout col="1" rows="auto, *, auto" class="text-col">
      <Label row="0" :text="event.title" textWrap="true" class="title" />
      <Label row="1">
        <FormattedString>
          <Span text="First published: " fontStyle="italic" />
          <Span :text="event.firstPublish" />
        </FormattedString>
      </Label>
      <GridLayout row="2" columns="auto, *, auto" class="more-row">
        <Label
          col="0"
          :text="`${event.allArticlesCount} ${
            allArticlesCount === 1 ? 'članak' : 'članaka'
          }`"
          class="num-articles"
        />
        <Label col="2" text="UPOREDITE NASLOVE" class="more-button" />
      </GridLayout>
    </GridLayout>
  </GridLayout>
</template>

<script>
import Event from './Event.vue';

export default {
  props: {
    event: {
      type: Object,
      required: true,
    },
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
.home-event-card {
  margin: 0 8 10 8;

  .image-col {
    horizontal-alignment: left;

    &,
    .image,
    .gradient {
      width: 120;
      height: 120;
    }

    .gradient {
      background-image: linear-gradient(to right, #e40001 0%, #4199fe 100%);
      opacity: 0.6;
    }
  }

  .text-col {
    height: 120;

    .title {
      font-size: 16;
      font-weight: 700;
    }

    .more-row {
      .num-articles,
      .more-button {
        padding-top: 5;
        padding-bottom: 5;
      }

      .num-articles {
        color: #e50001;
        padding-right: 8;
      }

      .more-button {
        border-radius: 12;
        padding-left: 10;
        padding-right: 25;
        background-color: #0177ff;
        background-image: url('res://arrow');
        background-repeat: no-repeat;
        background-position: right center;
        background-size: 52 25;
      }
    }
  }
}
</style>

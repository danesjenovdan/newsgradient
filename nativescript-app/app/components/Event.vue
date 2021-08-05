<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <Label :text="event.title" textWrap="true" class="event-title" />
    </ActionBar>
    <AbsoluteLayout class="main-view">
      <ListView
        for="article in articles"
        separatorColor="transparent"
        width="100%"
        height="100%"
      >
        <v-template>
          <StackLayout padding="0">
            <EventArticleCard :article="article" />
          </StackLayout>
        </v-template>
      </ListView>
    </AbsoluteLayout>
  </Page>
</template>

<script>
import EventArticleCard from './EventArticleCard.vue';
import temparticles from './temparticles';

export default {
  components: {
    EventArticleCard,
  },
  props: {
    event: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      articles: temparticles.articles,
    };
  },
};
</script>

<style lang="scss" scoped>
@import '@nativescript/theme/scss/variables';

.action-bar {
  @include colorize($background-color: 'background');

  .event-title {
    font-style: italic;
    margin: 8 40 0 40;
  }
}

.main-view {
  @include colorize($background-color: 'background-alt-5');
}
</style>

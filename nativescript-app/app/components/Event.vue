<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <Label :text="event.title" textWrap="true" class="event-title" />
    </ActionBar>

    <AbsoluteLayout class="main-view">
      <Spinner v-if="articles == null" />
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
import { fetchArticles } from '../services/api.service';
import Spinner from './Spinner.vue';
import EventArticleCard from './EventArticleCard.vue';

export default {
  components: {
    Spinner,
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
      articles: null,
    };
  },
  async mounted() {
    if (this.event && this.event.id) {
      const data = await fetchArticles(this.event.id);
      this.articles = (data && data.articles) || [];
    }
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

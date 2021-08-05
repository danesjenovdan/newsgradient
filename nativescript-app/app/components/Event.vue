<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <Label :text="event.title" textWrap="true" class="event-title" />
    </ActionBar>

    <GridLayout rows="*, auto" class="main-view">
      <Spinner v-if="articles == null" row="0" />
      <ListView
        v-else
        row="0"
        for="article in slantArticles"
        separatorColor="transparent"
      >
        <v-template>
          <StackLayout :padding="paddingForIndex($index)">
            <EventArticleCard :article="article" />
          </StackLayout>
        </v-template>
      </ListView>
      <GridLayout row="1" columns="*, *, *" class="slant-selector">
        <Button col="0" text="Left" @tap="onSlantTap(1)" />
        <Button col="1" text="Center" @tap="onSlantTap(2)" />
        <Button col="2" text="Right" @tap="onSlantTap(3)" />
      </GridLayout>
    </GridLayout>
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
      currentSlant: 2,
    };
  },
  computed: {
    slantArticles() {
      if (!this.articles) {
        return null;
      }
      const slant = String(this.currentSlant);
      return this.articles.filter((article) => article.medium.slant === slant);
    },
  },
  async mounted() {
    if (this.event && this.event.id) {
      const data = await fetchArticles(this.event.id);
      this.articles = (data && data.articles) || [];
    }
  },
  methods: {
    paddingForIndex(index) {
      if (index === 0) {
        return '8 8 4 8';
      }
      if (index === this.slantArticles.length - 1) {
        return '4 8 8 8';
      }
      return '4 8 4 8';
    },
    onSlantTap(slant) {
      this.currentSlant = slant;
    },
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

  .slant-selector {
    @include colorize($background-color: 'background-alt-10');

    padding: 10 40;
    height: 60;
  }
}
</style>

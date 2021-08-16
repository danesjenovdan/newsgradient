<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <Label :text="event.title" textWrap="true" class="event-title" />
    </ActionBar>

    <GridLayout rows="*, auto" class="main-view">
      <Spinner v-if="articles == null" row="0" />
      <Pager
        v-else
        row="0"
        :selectedIndex="currentSlantIndex"
        @selectedIndexChange="onSlantIndexChange"
      >
        <PagerItem>
          <ListView
            for="article in articlesBySlant['1']"
            separatorColor="transparent"
          >
            <v-template>
              <StackLayout :padding="paddingForIndex('1', $index)">
                <EventArticleCard :article="article" />
              </StackLayout>
            </v-template>
          </ListView>
        </PagerItem>
        <PagerItem>
          <ListView
            for="article in articlesBySlant['2']"
            separatorColor="transparent"
          >
            <v-template>
              <StackLayout :padding="paddingForIndex('2', $index)">
                <EventArticleCard :article="article" />
              </StackLayout>
            </v-template>
          </ListView>
        </PagerItem>
        <PagerItem>
          <ListView
            for="article in articlesBySlant['3']"
            separatorColor="transparent"
          >
            <v-template>
              <StackLayout :padding="paddingForIndex('3', $index)">
                <EventArticleCard :article="article" />
              </StackLayout>
            </v-template>
          </ListView>
        </PagerItem>
      </Pager>
      <GridLayout row="1" columns="*, *, *" class="slant-selector">
        <Button col="0" text="Left" @tap="onSlantTap(1)" />
        <Button col="1" text="Center" @tap="onSlantTap(2)" />
        <Button col="2" text="Right" @tap="onSlantTap(3)" />
      </GridLayout>
    </GridLayout>
  </Page>
</template>

<script>
import { groupBy } from 'lodash-es';
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
    currentSlantIndex() {
      return this.currentSlant - 1;
    },
    articlesBySlant() {
      return groupBy(this.articles, (a) => a.medium.slant);
    },
  },
  async mounted() {
    if (this.event && this.event.id) {
      // HACK: navigate animation lags out hard if articles load in the middle
      // of it, so delay loading until animation is done
      await new Promise((res) => setTimeout(res, 200));
      const data = await fetchArticles(this.event.id);
      this.articles = (data && data.articles) || [];
    }
  },
  methods: {
    paddingForIndex(slant, index) {
      if (index === 0) {
        return '8 8 4 8';
      }
      if (index === this.articlesBySlant[slant].length - 1) {
        return '4 8 8 8';
      }
      return '4 8 4 8';
    },
    onSlantTap(slant) {
      this.currentSlant = slant;
    },
    onSlantIndexChange(arg) {
      this.currentSlant = arg.object.selectedIndex + 1;
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

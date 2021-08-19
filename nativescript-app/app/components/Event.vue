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
      <GridLayout
        row="1"
        rows="auto, auto"
        columns="*, *, *"
        class="slant-selector"
      >
        <Button
          row="0"
          col="0"
          :class="['slant-button', { active: currentSlant === 1 }]"
          @tap="onSlantTap(1)"
        />
        <Button
          row="0"
          col="1"
          :class="['slant-button', { active: currentSlant === 2 }]"
          @tap="onSlantTap(2)"
        />
        <Button
          row="0"
          col="2"
          :class="['slant-button', { active: currentSlant === 3 }]"
          @tap="onSlantTap(3)"
        />
        <Label row="1" col="0" text="Lijevo" class="slant-label" />
        <Label row="1" col="1" text="Neutralno" class="slant-label" />
        <Label row="1" col="2" text="Desno" class="slant-label" />
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
    margin: 8 40 0 40;
    padding: 0;
    font-style: italic;
    text-align: center;
  }
}

.main-view {
  @include colorize($background-color: 'background-alt-5');

  .slant-selector {
    @include colorize($background-color: 'background-alt-10');

    padding: 10 40;
    height: 80;
    text-align: center;

    .slant-button {
      @include colorize($background-color: 'background');
      @include colorize($border-color: 'background');

      width: 35;
      height: 35;
      border-radius: 50%;
      border-style: solid;
      border-width: 5;
      margin-bottom: 4;
      padding: 4;

      &.active {
        background-color: #0177ff;
      }
    }

    .slant-label {
      @include colorize($color: 'primary');

      text-transform: uppercase;
      font-style: italic;
    }
  }
}
</style>

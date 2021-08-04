<template>
  <Page>
    <ActionBar flat="true">
      <Label :text="event.title" textWrap="true" class="event-title" />
    </ActionBar>

    <ScrollView>
      <StackLayout class="article-list">
        <EventArticleCard
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </StackLayout>
    </ScrollView>
  </Page>
</template>

<script>
import EventArticleCard from './EventArticleCard.vue';
import tempevents from './tempevents';
import temparticles from './temparticles';

export default {
  components: {
    EventArticleCard,
  },
  props: {
    event: {
      type: Object,
      default: tempevents[0],
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
.event-title {
  font-style: italic;
  margin: 8 40 0 40;
}

.article-list {
  padding: 10 8;
}
</style>

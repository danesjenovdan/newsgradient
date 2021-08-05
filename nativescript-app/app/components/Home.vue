<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <NSImg src="res://logo_text" stretch="aspectFit" class="logo-text" />
    </ActionBar>

    <GridLayout rows="auto, *" class="main-view">
      <Label
        row="0"
        text="Pet najaktuelnijih vijesti u izvještajima bosanskohercegovačkih medija, poredanih po ideološkoj orijentaciji"
        textWrap="true"
        class="info"
      />
      <Spinner v-if="events == null" row="1" />
      <ListView row="1" for="event in events" separatorColor="transparent">
        <v-template>
          <StackLayout padding="0">
            <HomeEventCard :event="event" />
          </StackLayout>
        </v-template>
      </ListView>
    </GridLayout>
  </Page>
</template>

<script>
import { fetchTopEvents } from '../services/api.service';
import Spinner from './Spinner.vue';
import HomeEventCard from './HomeEventCard.vue';

export default {
  components: {
    Spinner,
    HomeEventCard,
  },
  data() {
    return {
      events: null,
    };
  },
  async mounted() {
    const data = await fetchTopEvents();
    this.events = data || [];
  },
};
</script>

<style lang="scss" scoped>
@import '@nativescript/theme/scss/variables';

.action-bar {
  @include colorize($background-color: 'background');

  .logo-text {
    margin: 18 0 0 0;
    width: 175;
    height: 25;
  }
}

.main-view {
  @include colorize($background-color: 'background-alt-5');

  .info {
    margin: 10 60;
    text-align: center;
  }
}
</style>

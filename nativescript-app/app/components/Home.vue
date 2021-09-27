<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <NSImg src="res://logo_text" stretch="aspectFit" class="logo-text" />
      <ActionItem text="Više o" android.position="popup" @tap="onAboutTap" />
      <ActionItem text="Kontakt" android.position="popup" @tap="onContactTap" />
      <!-- <ActionItem
        text="Toggle dark mode"
        android.position="popup"
        @tap="toggleTheme"
      /> -->
      <ActionItem
        text="Osvježi izvještaje"
        android.position="popup"
        @tap="refreshEvents"
      />
    </ActionBar>

    <GridLayout rows="auto, *" class="main-view">
      <Label
        row="0"
        text="Najaktuelnije vijesti u izvještajima bosanskohercegovačkih medija grupisane po ideološkoj orijentaciji."
        textWrap="true"
        class="info"
      />
      <Spinner v-if="events == null" row="1" />
      <ListView row="1" for="event in events" separatorColor="transparent">
        <v-template>
          <StackLayout :padding="paddingForIndex($index)">
            <HomeEventCard :event="event" />
          </StackLayout>
        </v-template>
      </ListView>
    </GridLayout>
  </Page>
</template>

<script>
import { loadAndSetTheme, toggleAndSaveTheme } from '../services/theme.service';
import { fetchTopEvents } from '../services/api.service';
import { setMessageReceivedListener } from '../services/notifications.service';
import About from './About.vue';
import Contact from './Contact.vue';
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
    loadAndSetTheme();

    await this.refreshEvents();

    setMessageReceivedListener(() => {
      this.refreshEvents();
    });
  },
  methods: {
    async refreshEvents() {
      this.events = null;
      const data = await fetchTopEvents();
      this.events = data || [];
    },
    paddingForIndex(index) {
      if (index === 0) {
        return '8 8 4 8';
      }
      if (index === this.events.length - 1) {
        return '4 8 8 8';
      }
      return '4 8 4 8';
    },
    onAboutTap() {
      this.$navigateTo(About, {
        transition: {
          name: 'slideLeft',
          duration: 200,
          curve: 'easeInOut',
        },
      });
    },
    onContactTap() {
      this.$navigateTo(Contact, {
        transition: {
          name: 'slideleft',
          duration: 200,
          curve: 'easeInOut',
        },
      });
    },
    toggleTheme() {
      toggleAndSaveTheme();
    },
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

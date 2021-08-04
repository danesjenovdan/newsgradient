<template>
  <Page>
    <ActionBar flat="true">
      <Image src="res://logo_text" stretch="aspectFit" class="logo-text" />
    </ActionBar>

    <ScrollView>
      <GridLayout rows="auto, *">
        <Label
          row="0"
          text="Pet najaktuelnijih vijesti u izvještajima bosanskohercegovačkih medija, poredanih po ideološkoj orijentaciji"
          textWrap="true"
          class="info"
        />
        <StackLayout row="1">
          <HomeEventCard
            v-for="event in events"
            :key="event.id"
            :event="event"
          />
        </StackLayout>
      </GridLayout>
    </ScrollView>
  </Page>
</template>

<script>
import HomeEventCard from './HomeEventCard.vue';
import tempevents from './tempevents';

export default {
  components: {
    HomeEventCard,
  },
  data() {
    return {
      events: tempevents,
    };
  },
};
</script>

<style lang="scss" scoped>
.logo-text {
  margin: 18 0 0 0;
  width: 175;
  height: 25;
}

.info {
  margin: 15 60;
  text-align: center;
}
</style>

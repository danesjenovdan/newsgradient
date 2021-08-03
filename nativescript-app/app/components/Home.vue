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
          <HomeEventCard v-for="(event, i) in events" :key="i" />
        </StackLayout>
      </GridLayout>
    </ScrollView>
  </Page>
</template>

<script>
import HomeEventCard from './HomeEventCard.vue';

export default {
  components: {
    HomeEventCard,
  },
  data() {
    return {
      events: Array(50),
    };
  },
};
</script>

<style lang="scss" scoped>
// @import '@nativescript/theme/scss/variables/blue';

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

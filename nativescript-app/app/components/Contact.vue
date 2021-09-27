<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <Label text="Kontakt" textWrap="true" class="title" />
    </ActionBar>
    <ScrollView>
      <StackLayout class="main-view">
        <GridLayout rows="auto, auto" class="title-container">
          <Label row="0" text="Danes je nov dan, Inštitut za druga vprašanja" textWrap="true" class="title" />
          <StackLayout row="1" class="gradient-line" />
        </GridLayout>
        <StackLayout class="content-container">
          <HtmlView :html="kontaktHtml" />
        </StackLayout>
      </StackLayout>
    </ScrollView>
  </Page>
</template>

<script>
export default {
  data() {
    return {
      kontaktHtml: `
        <div style="text-align: center;">
          <a href="mailto:newsgradient@danesjenovdan.si" target="_blank">newsgradient@danesjenovdan.si</a>
        </div>
        <div style="text-align: center;">
          <a href="tel:+38664147823" target="_blank">+38664147823</a>
        </div>
      `,
    };
  },
};
</script>

<style lang="scss" scoped>
@import '@nativescript/theme/scss/variables';

.action-bar {
  @include colorize($background-color: 'background');

  .title {
    margin: 8 40 0 40;
    padding: 0;
    font-style: italic;
    text-align: center;
  }
}

.main-view {
  @include colorize($background-color: 'background-alt-5');

  .title-container {
    margin: 12 40 0 40;

    .title {
      font-size: 14;
      font-weight: 700;
      text-align: center;
      text-transform: uppercase;
    }

    .gradient-line {
      height: 2;
      background-image: linear-gradient(to right, #0076fe 0%, #e50001 100%);
    }
  }

  .content-container {
    @include colorize($background-color: 'background');

    padding-top: 30;
    font-size: 16;

    padding-bottom: 0;
  }
}
</style>

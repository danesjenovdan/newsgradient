<template>
  <GridLayout columns="auto, auto" class="social-score-badge">
    <NSImg col="0" stretch="aspectFit" src="res://twitter" class="image" />
    <Label col="1" :text="text" class="text" />
  </GridLayout>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
@import '@nativescript/theme/scss/variables';

.social-score-badge {
  padding: 0 8 0 10;
  border-radius: 12;
  background-color: #f6f6f6;

  .image {
    width: 13;
    height: 10;
    margin-right: 6;
  }

  .text {
    padding: 5 0;
    color: #000;
  }
}
</style>

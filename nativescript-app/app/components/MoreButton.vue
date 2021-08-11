<template>
  <GridLayout columns="auto, auto" class="more-button">
    <Label col="0" :text="text" class="text" />
    <NSImg col="1" stretch="aspectFit" src="res://arrow" class="image" />
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
.more-button {
  padding: 0 8 0 10;
  border-radius: 12;
  background-color: #0177ff;

  .image {
    width: 13;
    height: 10;
    margin-left: 6;
  }

  .text {
    padding: 5 0;
    text-transform: uppercase;
    color: #fff;
  }
}
</style>

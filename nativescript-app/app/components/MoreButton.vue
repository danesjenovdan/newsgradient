<template>
  <Label :text="text" class="more-button" />
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
  padding: 5 25 5 10;
  border-radius: 12;
  background-color: #0177ff;
  background-image: url('res://arrow');
  background-repeat: no-repeat;
  background-position: right center;
  background-size: 52 25;
  text-transform: uppercase;
  color: #fff;
}
</style>

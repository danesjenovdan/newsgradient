<template>
  <GridLayout columns="120, *" class="home-event-card">
    <Image
      col="0"
      src="res://logo"
      stretch="aspectFit"
      class="image"
      width="120"
      height="120"
    />
    <GridLayout col="1" rows="*, *" class="text-col">
      <Label row="0" text="first" backgroundColor="#43b883" />
      <Label row="1" text="first" backgroundColor="#f00" />
    </GridLayout>
  </GridLayout>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.home-event-card {
  margin: 0 8 10 8;

  .image {
    margin-right: 10;
    width: 120;
    height: 120;
  }

  // .text-col {
  //   margin-left: 8;
  // }
}
</style>

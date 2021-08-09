<template>
  <Label :text="text" textWrap="true" @loaded="onLoaded" />
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
    maxLines: {
      type: Number,
      required: true,
    },
  },
  methods: {
    onLoaded(arg) {
      const label = arg.object;
      if (label.android) {
        // eslint-disable-next-line no-undef
        const { TruncateAt } = android.text.TextUtils;
        label.android.setEllipsize(TruncateAt.END);
        label.android.setMaxLines(this.maxLines);
      } else if (label.ios) {
        label.ios.numberOfLines = this.maxLines;
      }
    },
  },
};
</script>

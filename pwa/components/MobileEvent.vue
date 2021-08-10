<template>
  <div class="card flex" @click="$router.push('/events/' + eventUri)">
    <div class="flex">
      <div class="image-ratio">
        <div
          :style="{
            backgroundImage: `linear-gradient(to right, rgba(228, 0, 1, 0.6) 0%, rgba(65, 153, 254, 0.6) 100%), url(https://images.weserv.nl/?url=${imageUrl}&w=120&h=120&fit=cover)`,
          }"
          class="article-image"
        ></div>
      </div>
      <div class="card__body flex flex--column flex-justify--space-between">
        <div>
          <div class="card__text-wrapper">
            <span class="card__title"> {{ title | trim }} </span>
          </div>
          <span v-if="firstPublish" class="text--italic">First published: </span>{{ firstPublish }}
        </div>
        <div>
          <div class="flex flex-justify--space-between flex-align--center">
            <div class="flex flex-column">
              <span class="articles">{{ `${allArticlesCount} ${allArticlesCount === 1 ? 'članak' : 'članaka'}` }}</span>
              <div>
                <span class="social-score-badge badge"
                  >{{ socialScore }}
                  <i class="icon" />
                </span>
              </div>
            </div>
            <button
              :to="'/events/' + eventUri"
              class="more-button text--uppercase flex flex-align--center"
              @click="$router.push('/events/' + eventUri)"
            >
              Uporedite naslove
              <img src="@/assets/svg/puscica-bela.svg" style="vertical-align: inherit; width: 12px; margin-left: 2px" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MobileEvent',
  filters: {
    trim(value) {
      if (value.toString().length <= 70) {
        return value
      }
      return value.toString().slice(0, 70) + ' ...'
    },
  },
  props: {
    imageUrl: {
      type: String,
      default: '',
    },
    title: {
      type: String,
      default: '',
    },
    firstPublish: {
      type: String,
      default: '',
    },
    eventUri: {
      type: String,
      default: '',
    },
    articleCount: {
      type: Number,
      default: 0,
    },
    allArticlesCount: {
      type: Number,
      default: 0,
    },
    socialScore: {
      type: Number,
      default: 0,
    },
  },
  mounted() {
    this.$store.dispatch('carousel/setSlant', 2)
  },
}
</script>

<style lang="scss" scoped>
.card {
  background: white;
  width: 100%;
  text-overflow: ellipsis;
  overflow: hidden;
  border-right: none;
  border-left: none;
  border-radius: 0;
  margin-bottom: 10px;
  font-weight: 300;

  .image-ratio {
    width: 120px;

    .article-image {
      height: 0;
      padding-top: 120px;
      width: 110px;
      background-position: center center;
      background-size: cover;
      position: relative;
    }
  }

  &--small {
    background: transparent;
    width: 100%;
    border: 1px solid black;
    border-radius: 0;
  }

  &__body {
    width: 90%;
    margin: 10px;
  }

  &__image {
    width: 100px;
    height: 80px;
  }

  &__header {
    width: 90%;
  }

  &__title {
    font-size: 16px;
    font-weight: 900;
    line-height: 1.1;
    color: #3f3942;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
    padding-bottom: 0.18em;
  }

  &__text {
    font-size: 0.8rem;
  }

  .social-score-badge {
    display: inline-flex;
    align-items: center;
    background-color: #f6f6f6;
    border-radius: 5em;
    padding: 4px 6px;
    font-size: 12px;
    font-weight: 400;

    .icon {
      display: inline-block;
      margin-left: 4px;
      width: 14px;
      height: 14px;
      background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%23000" d="M18.9 7c.8-.5 1.3-1.2 1.6-2-.8.4-1.6.7-2.4.9-.7-.8-1.6-1.1-2.7-1.1-1 0-1.9.4-2.6 1.1a3.63 3.63 0 00-1 3.4c-3-.2-5.5-1.5-7.5-3.9-.4.6-.6 1.2-.6 1.8 0 1.3.5 2.3 1.6 3.1-.6-.1-1.2-.2-1.6-.5 0 .9.3 1.7.8 2.4s1.3 1.1 2.1 1.3c-.3.1-.6.1-1 .1-.3 0-.5 0-.7-.1.2.8.7 1.4 1.3 1.8.6.5 1.3.7 2.2.7-1.3 1-2.9 1.6-4.6 1.6h-.9c1.7 1.1 3.6 1.6 5.7 1.6a10.23 10.23 0 009.3-5.6c.8-1.6 1.2-3.2 1.2-4.9v-.4c.8-.6 1.4-1.2 1.8-1.9-.6.3-1.3.5-2 .6z"/></svg>');
    }
  }
}

.articles {
  font-size: 12px;
  color: #e50001;
  font-weight: 400;
}
</style>

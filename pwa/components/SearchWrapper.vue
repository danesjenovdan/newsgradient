<template>
  <div class="event-wrapper flex flex--column">
    <Divider class="w-100" />
    <div class="content-wrapper-custom">
      <div class="flex flex--column flex-justify--center">
        <div :class="{ 'title--small': !isMain }" class="title">
          {{ title }}
        </div>
        <div class="mt8 mb8">
          <span class="articles">{{ `${allArticlesCount} ${allArticlesCount === 1 ? 'članak' : 'članaka'}` }}</span>
        </div>
        <div v-if="isMain" :class="['mt-2', { empty__wrapper: !articleCount, row: articleCount }]">
          <template v-if="articleCount">
            <div v-for="article in articles" :key="article.id" class="col-lg-4 col-md-6 mb-4">
              <ArticleCard
                :title="article.title"
                :content="article.content"
                :image-url="article.image"
                :source-title="article.medium?.title"
                :article-url="article.url"
                :favicon-url="article.medium?.favicon"
                :medium-url="article.medium?.uri"
                :medium-name="article.medium?.title"
                :social-score="article.social_score"
                class="article-wrapper"
              />
            </div>
          </template>
        </div>
        <div v-else :class="{ empty__wrapper: !articleCount }" class="flex flex--column mt-2 small-articles">
          <template v-if="articleCount">
            <ArticleCardSmall
              v-for="article in articles"
              :key="article.id"
              :title="article.title"
              :content="article.content"
              :image-url="article.image"
              :source-title="article.medium?.title"
              :article-url="article.url"
              :favicon-url="article.medium?.favicon"
              :medium-url="article.medium?.uri"
              :medium-name="article.medium?.title"
              :only-one="articles.length === 1"
              :social-score="article.social_score"
              class="article-wrapper"
            />
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Divider from './Divider'
import ArticleCard from './ArticleCard'
import ArticleCardSmall from './ArticleCardSmall'

export default {
  name: 'EventWrapper',
  components: { ArticleCardSmall, ArticleCard, Divider },
  props: {
    isMain: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      default: 'No title',
    },
    firstPublish: {
      type: String,
      default: '20 hours ago',
    },
    articleCount: {
      type: Number,
      default: 0,
    },
    allArticlesCount: {
      type: Number,
      default: 0,
    },
    eventUri: {
      default: 'uri',
      type: String,
      required: true,
    },
    articles: {
      type: Array,
      default: () => [],
    },
    socialScore: {
      type: Number,
      default: 0,
    },
  },
}
</script>

<style scoped lang="scss">
.wrapper {
  margin: 10px;
}

.title {
  font-size: 36px;
  font-weight: 900;
  font-style: italic;
  color: #3f3942;
  display: block;
  line-height: 1.1;

  &--small {
    font-size: 27px;
  }
}

.articles {
  font-size: 18px;
  color: #e50001;
}

.content-wrapper-custom {
  padding: 25px 25px;
  height: 100%;
  min-height: 808px;
  display: flex;
  justify-content: space-between;
  flex-direction: column;
}

.event-wrapper {
  min-height: 600px;
  height: 100%;
  background-color: #f6f6f6;
}

.empty {
  &__holder {
    margin-top: 40%;
    &--main {
      margin-top: 22%;
    }
  }

  &__wrapper {
    height: 100%;
    // border-top: 1px solid black;
  }

  &__text {
    margin-top: 8px;
    font-weight: 300;
    font-style: italic;
    font-size: 22px;
    max-width: 350px;
    text-align: center;
    line-height: 1.1;
  }
}

.article-wrapper {
  height: 100%;
}

.small-articles {
  margin-left: -25px;
  margin-right: -25px;

  .article-wrapper {
    padding-left: 25px;
    padding-right: 25px;
    padding-top: 14px;
    padding-bottom: 20px;
  }
}

.missing-icon {
  width: 70px;
}
</style>

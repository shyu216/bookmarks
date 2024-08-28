<template>
  <v-tooltip :text="bookmark.href">
    <template v-slot:activator="{ props }">
      <v-card
        class="mx-auto"
        elevation="12"
        :subtitle="
          new Date(parseInt(bookmark.add_date) * 1000).toLocaleDateString()
        "
        :title="bookmark.title"
        :href="bookmark.href"
        target="_blank"
        append-icon="fas fa-link"
        hover
        link
        v-bind="props"
      >
        <template v-slot:prepend>
          <v-avatar>
            <v-img
              alt=""
              :src="
                bookmark.icon
                  ? bookmark.icon
                  : '@/../public/icon/android-chrome-192x192.png'
              "
            ></v-img>
          </v-avatar>
        </template>
        <v-card-text>{{ bookmark.description }}</v-card-text>
      </v-card>
    </template>
  </v-tooltip>
</template>

<script>
export default {
  props: ["bookmark"],
};
</script>

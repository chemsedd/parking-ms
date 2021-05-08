import Vue from "vue";

// or import all icons if you don't care about bundle size
import "vue-awesome/icons";

// CSS file
import Icon from "vue-awesome/components/Icon";

// globally (in your main .js file)
Vue.component("v-icon", Icon);

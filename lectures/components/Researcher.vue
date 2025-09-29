<script setup>
import { useSlideContext } from '@slidev/client'
const { $slidev } = useSlideContext()

defineProps({
  rImg: { type: String, required: true },
  rName: { type: String, required: true },
  rField: { type: String, required: false},
  rclass:{type: String, default:""},
})
</script>

<template>
    <div :class="`flex flex-col items-center ${rclass} `">
        <img :src="rImg" class="centered-rounded" />
        <div class="text-sm opacity-70 text-center">
            {{ rName }} <br /> {{ rField }}
        </div>
    </div>
</template>

<!-- 
  rml:{type: Number, default: 40},
  rmt:{type: Number, default: 7},
  rmtNegative: { type: Boolean, default: true },

ml-${rml} ${rmtNegative ? '-mt-' : 'mt-'}${rmt} 
-->
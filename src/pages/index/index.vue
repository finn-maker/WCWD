<template>
	<view class="content" @click="goToDiary">
		<image class="bg" src="/static/bg.png" mode="aspectFill" />
		<view class="text-overlay">
			<text class="thinking-text">在想什么...</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {

		},
		methods: {
			goToDiary() {
				uni.navigateTo({
					url: '/pages/diary/diary'
				})
			}
		}
	}
</script>

<style>
	.content {
		width: 100%;
		height: 100vh;
		position: relative;
		overflow: hidden;
	}

	.bg {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		z-index: 1;
		object-fit: cover;
	}

	.text-overlay {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		z-index: 2;
		text-align: center;
	}

	.thinking-text {
		font-size: 48rpx;
		color: #333;
		font-weight: bold;
		text-shadow: 2rpx 2rpx 4rpx rgba(255, 255, 255, 0.8);
	}
</style>

<template>
    <view class="diary">
        <image class="WaterPerson" src="/static/WaterPerson.png" mode="aspectFill" />
        <view class="text-container">
            <image class="Text" src="/static/text2.png" mode="aspectFill" />
            <view class="diary-input-container">
                <text v-if="currentStep === 'greeting'" class="greeting-text">{{ greetingText }}</text>
                <text v-if="currentStep === 'weather'" class="weather-question">天气怎么样呢？</text>
                <text v-if="currentStep === 'mood'" class="mood-question">今天感受怎么样？</text>
                <text v-if="currentStep === 'thinking'" class="thinking-question">在想什么....？</text>
                <text v-if="currentStep === 'theme'" class="theme-question">今天想一个主题吧</text>
                <text v-if="currentStep === 'goodbye'" class="goodbye-text">{{ goodbyeText }}</text>
            </view>
            
            <!-- 天气选择 - 移到 Text 内部 -->
            <view v-if="currentStep === 'weather'" class="choice-container-in-text">
                <view class="choice-item-in-text" @click="selectWeather('很好')">
                    <text>很好</text>
                </view>
                <view class="choice-item-in-text" @click="selectWeather('一般')">
                    <text>一般</text>
                </view>
                <view class="choice-item-in-text" @click="selectWeather(weatherReplacement)">
                    <text>{{ weatherReplacement }}</text>
                </view>
            </view>
            
            <!-- 心情选择 - 移到 Text 内部 -->
            <view v-if="currentStep === 'mood'" class="mood-container-in-text">
                <view class="mood-item-in-text" @click="selectMood('great')">
                    <image src="/static/appleFace/great.png" mode="aspectFit" class="mood-image" />
                </view>
                <view class="mood-item-in-text" @click="selectMood('happy')">
                    <image src="/static/appleFace/happy.png" mode="aspectFit" class="mood-image" />
                </view>
                <view class="mood-item-in-text" @click="selectMood('nomal')">
                    <image src="/static/appleFace/nomal.png" mode="aspectFit" class="mood-image" />
                </view>
                <view class="mood-item-in-text" @click="selectMood('sad')">
                    <image src="/static/appleFace/sad.png" mode="aspectFit" class="mood-image" />
                </view>
                <view class="mood-item-in-text" @click="selectMood('angry')">
                    <image src="/static/appleFace/angry.png" mode="aspectFit" class="mood-image" />
                </view>
            </view>
            
            <!-- 主题输入 - 移到 Text 内部 -->
            <view v-if="currentStep === 'theme'" class="theme-container-in-text">
                <input 
                    class="theme-input-in-text" 
                    v-model="themeText" 
                    placeholder="输入主题..."
                    placeholder-style="color: #999;"
                    maxlength="20"
                />
                <view class="theme-confirm-btn" @click="confirmTheme">
                    <text>确认</text>
                </view>
            </view>
        </view>
        <image class="bg-image" src="/static/diary.png" mode="aspectFill" />
        
        <!-- 完成按钮 - 移到背景图片右下角 -->
        <view v-if="currentStep === 'thinking' && moodText.trim()" class="complete-btn" @click="completeThinking">
            <text>完成</text>
        </view>
        
        <!-- 固定排版盒子 -->
        <view class="info-box">
            <view class="info-content">
                <text class="date-text">{{ currentDate }}</text>
                <text class="weather-text">{{ weatherText }}</text>
                <text class="mood-label">心情</text>
                <view class="mood-emoji-container">
                    <image :src="`/static/appleFace/${selectedMood}.png`" mode="aspectFit" class="mood-emoji-image" />
                </view>
            </view>
        </view>
        
        <!-- 心情输入框盒子 -->
        <view v-if="currentStep === 'thinking'" class="mood-input-box">
            <textarea 
                class="mood-input" 
                v-model="moodText" 
                :placeholder="showPlaceholder ? '记录今天的心情...' : ''"
                placeholder-style="color: #999;"
                :maxlength="240"
                :show-confirm-bar="false"
                :adjust-position="false"
                :cursor-spacing="0"
                :hold-keyboard="false"
                :disable-default-padding="true"
                @input="onMoodInput"
                @focus="onFocus"
                @blur="onBlur"
            />
        </view>
    </view>
</template>

<script>
export default {
    name: 'Diary',
    data() {
        return {
            diaryText: '',
            moodText: '',
            currentDate: '',
            showPlaceholder: true, // 控制占位符的显示
            currentStep: 'greeting', // 当前对话步骤
            greetingText: '早上好！',
            goodbyeText: '再见！',
            weatherText: '天气晴 ☀️',
            weatherReplacement: '糟透了',
            selectedMood: 'great', // 默认使用 great 图片
            themeText: '',
            userName: '我的朋友', // 用户名，默认为我的朋友
            currentTime: '',
            currentHour: 0
        }
    },
    onLoad() {
        this.getCurrentDate()
        this.getCurrentTime()
        this.startConversation()
    },
    methods: {
        goBack() {
            uni.navigateBack()
        },
        getCurrentDate() {
            const now = new Date()
            const year = now.getFullYear()
            const month = now.getMonth() + 1
            const day = now.getDate()
            this.currentDate = `${year}年${month}月${day}日`
        },
        getCurrentTime() {
            const now = new Date()
            this.currentHour = now.getHours()
            this.currentTime = `${now.getHours()}:${now.getMinutes()}`
            
            // 模拟获取天气信息（实际项目中应该调用天气API）
            this.getWeatherInfo()
        },
        getWeatherInfo() {
            // 这里模拟天气数据，实际项目中应该调用天气API
            const mockWeather = {
                condition: '晴', // 天气状况：晴、雨、雪、阴等
                temperature: 28, // 温度
                wind: '微风' // 风力
            }
            
            // 根据天气情况设置替换文本
            if (mockWeather.condition === '晴' && mockWeather.temperature > 26) {
                this.weatherReplacement = '晒死我了'
            } else if (mockWeather.condition.includes('雨')) {
                this.weatherReplacement = '淋湿了'
            } else if (mockWeather.condition === '雪' || mockWeather.temperature < 10) {
                this.weatherReplacement = '好冷'
            } else if (mockWeather.wind.includes('大') || mockWeather.wind.includes('强')) {
                this.weatherReplacement = '风超级大'
            } else if (mockWeather.condition.includes('雨') || mockWeather.condition.includes('雪') || mockWeather.wind.includes('大')) {
                this.weatherReplacement = '出不了门'
            } else {
                this.weatherReplacement = '糟透了'
            }
            
            // 设置天气显示文本
            this.weatherText = `天气${mockWeather.condition} ${this.getWeatherEmoji(mockWeather.condition)}`
        },
        getWeatherEmoji(condition) {
            const emojiMap = {
                '晴': '☀️',
                '雨': '🌧️',
                '雪': '❄️',
                '阴': '☁️',
                '雾': '🌫️'
            }
            return emojiMap[condition] || '🌤️'
        },
        startConversation() {
            // 根据时间设置问候语
            if (this.currentHour >= 5 && this.currentHour < 12) {
                this.greetingText = `${this.userName}早上好！`
            } else if (this.currentHour >= 12 && this.currentHour < 18) {
                this.greetingText = `${this.userName}下午好！`
            } else {
                this.greetingText = `${this.userName}晚上好！`
            }
            
            // 设置告别语
            if (this.currentHour >= 18 || this.currentHour < 5) {
                this.goodbyeText = `${this.userName}晚安，明天见`
            } else {
                this.goodbyeText = `${this.userName}一会见~`
            }
            
            // 3秒后进入天气选择
            setTimeout(() => {
                this.currentStep = 'weather'
            }, 3000)
        },
        selectWeather(weather) {
            // 天气选择不影响 info-box 显示，保持原来的天气信息
            this.currentStep = 'mood'
        },
        selectMood(mood) {
            this.selectedMood = mood
            this.currentStep = 'thinking'
        },
        // 监听输入框内容变化，限制行数
        onMoodInput(e) {
            const text = e.detail.value
            const lines = text.split('\n')
            
            // 严格限制在10行以内
            if (lines.length > 10) {
                // 如果超过10行，只保留前10行
                this.moodText = lines.slice(0, 10).join('\n')
                // 显示提示
                uni.showToast({
                    title: '最多只能输入10行',
                    icon: 'none',
                    duration: 2000
                })
            } else {
                this.moodText = text
            }
            
            // 当有内容时隐藏占位符
            if (text.trim()) {
                this.showPlaceholder = false
            }
        },
        
        // 手动完成输入
        completeThinking() {
            if (this.moodText.trim()) {
                this.currentStep = 'theme'
                uni.showToast({
                    title: '心情记录完成',
                    icon: 'success',
                    duration: 1500
                })
            } else {
                uni.showToast({
                    title: '请先输入一些内容',
                    icon: 'none',
                    duration: 1500
                })
            }
        },
        onFocus() {
            // 当获得焦点时隐藏占位符
            this.showPlaceholder = false
        },
        onBlur() {
            // 当失去焦点且没有内容时显示占位符
            if (!this.moodText.trim()) {
                this.showPlaceholder = true
            }
        },
        confirmTheme() {
            if (this.themeText.trim()) {
                this.currentStep = 'goodbye'
            } else {
                uni.showToast({
                    title: '主题不能为空',
                    icon: 'none'
                })
            }
        }
    }
}
</script>

<style scoped>
.diary {
    width: 100%;
    height: 100vh;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.text-container {
    position: absolute;
    top: 7%;
    left: 25%;
    width: 367rpx;
    height: 124rpx;
    z-index: 2;
}

.Text {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.diary-input-container {
    position: absolute;
    top: 17%;
    left: 12%;
    width: 80%;
    height: 60%;
    background: transparent;
    border: none;
    outline: none;
    font-size: 24rpx;
    color: #37aaa4;
    text-align: center;
    line-height: 1.4;
    z-index: 3;
}

.greeting-text {
    font-size: 24rpx;
    color: #37aaa4;
    font-weight: bold;
    position: relative;
    top: 20rpx;
}

.weather-question {
    font-size: 20rpx;
    color: #37aaa4;
}

.mood-question {
    font-size: 20rpx;
    color: #37aaa4;
}

.thinking-question {
    font-size: 20rpx;
    color: #37aaa4;
    position: relative;
    top: 20rpx;
}

.theme-question {
    font-size: 20rpx;
    color: #37aaa4;
}

.goodbye-text {
    font-size: 24rpx;
    color: #37aaa4;
    font-weight: bold;
    position: relative;
    top: 20rpx;
}

.info-box {
    position: absolute;
    top: 25%;
    left: 50%;
    transform: translateX(-50%);
    width: 57%;
    max-width: 600rpx;
    background: transparent;
    border-radius: 20rpx;
    padding: 30rpx;
    z-index: 3;
}

.info-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20rpx;
}

.date-text {
    font-size: 24rpx;
    color: #333;
    font-weight: bold;
}

.weather-text {
    font-size: 20rpx;
    color: #666;
}

.mood-label {
    font-size: 20rpx;
    color: #666;
}

.mood-emoji {
    font-size: 24rpx;
}

.mood-emoji-container {
    display: flex;
    align-items: center;
    gap: 10rpx;
}

.mood-emoji-image {
    width: 30rpx;
    height: 30rpx;
}

.choice-container-in-text {
    position: absolute;
    top: 45%;
    left: 16%;
    width: 70%;
    height: 60rpx;
    display: flex;
    justify-content: space-around;
    align-items: center;
    z-index: 3;
}

.choice-item-in-text {
    width: 80rpx;
    height: 40rpx;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 10rpx;
    background: transparent;
    border: none;
    font-size: 20rpx;
    color: #333;
    font-weight: bold;
    transition: all 0.3s ease;
}

.choice-item-in-text:active {
    transform: scale(0.95);
}

.mood-container-in-text {
    position: absolute;
  top: 45%;
    left: 16%;
    width: 70%;
    height: 60rpx;
    display: flex;
    justify-content: space-around;
    align-items: center;
    z-index: 3;
}

.mood-item-in-text {
    width: 40rpx;
    height: 50rpx;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    background: transparent;
    border: none;
    font-size: 24rpx;
    transition: all 0.3s ease;
}

.mood-item-in-text:active {
    transform: scale(0.9);
}

.mood-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.theme-container-in-text {
    position: absolute;
    top: 45%;
    left: 16%;
    width: 70%;
    height: 60rpx;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 3;
}

.theme-input-in-text {
    flex: 1;
    height: 40rpx;
    background: transparent;
    border: none;
    outline: none;
    font-size: 20rpx;
    color: #37aaa4;
    padding: 0 10rpx;
    margin-right: 10rpx;
}

.theme-confirm-btn {
    width: 60rpx;
    height: 40rpx;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 10rpx;
    background: transparent;
    border: none;
    font-size: 18rpx;
    color: #37aaa4;
    font-weight: bold;
    transition: all 0.3s ease;
}

.theme-confirm-btn:active {
    transform: scale(0.95);
}

.complete-btn {
    position: absolute;
    bottom: 18%;
    right: 4%;
    width: 120rpx;
    height: 60rpx;
    background: rgba(102, 126, 234, 0.9);
    border-radius: 30rpx;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 4;
    box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.complete-btn:active {
    transform: scale(0.95);
}

.complete-btn text {
    color: white;
    font-size: 28rpx;
    font-weight: bold;
}

.mood-input-box {
    position: absolute;
    bottom: 24%;
    left: 50%;
    transform: translateX(-50%);
    width: 57%;
    height: 44%;
    z-index: 3;
    /* 以下属性可以移除或修改 */
    /* background: transparent; */
    /* border-radius: 20rpx; */
    /* display: flex; (移除) */
    /* align-items: flex-start; (移除) */
    /* justify-content: flex-start; (移除) */
    /* overflow: hidden; (移除) */
}

.mood-input {
    width: 100%;
    height: 600rpx; /* 固定高度：10行 * 60rpx = 600rpx */
    background: transparent;
    border: none;
    outline: none;
    resize: none;
    box-sizing: border-box;

    font-size: 30rpx;
    color: #333;
    text-align: left;
    
    /* -- 关键修改 -- */
    line-height: 60rpx; /* 使用倍数，而不是固定 rpx 值 */
    padding: 10rpx; /* 在四周增加一点内边距，让光标和文字有呼吸空间 */
    
    /* -- 移除以下冲突或多余的样式 -- */
    /* position: absolute; (移除) */
    /* vertical-align: top; (移除) */
    /* text-indent: 0; (移除) */
    /* white-space: pre-wrap; (默认行为) */
    /* word-wrap: break-word; (默认行为) */
}

.WaterPerson {
    position: absolute;
    top: 9%;
    left: 2%;
    width: 200rpx;
    height: 200rpx;
    z-index: 2;
    object-fit: cover;
    transform: scaleX(-1);
}

.bg-image {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-45%, -50%);
    width: 137%;
    height:69%;
    z-index: 1;
    object-fit: cover;
    object-position: center;
}

.diary-content {
    position: relative;
    z-index: 2;
    padding: 40rpx;
    background: rgba(255, 255, 255, 0.9);
    min-height: 100vh;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 40rpx;
}

.diary-title {
    font-size: 48rpx;
    font-weight: bold;
    color: #333;
}

.back-btn {
    background: #667eea;
    padding: 20rpx 30rpx;
    border-radius: 10rpx;
}

.back-text {
    color: white;
    font-size: 28rpx;
}

.diary-text {
    font-size: 32rpx;
    line-height: 1.8;
    color: #666;
    background: white;
    padding: 40rpx;
    border-radius: 20rpx;
    box-shadow: 0 4rpx 20rpx rgba(0, 0, 0, 0.1);
}
</style>
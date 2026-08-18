# Convert Website to Mobile App Prompt

## 簡介

The Convert Website to Mobile App Prompt is a free AI prompt that generates production-ready hybrid mobile app architectures for developers converting websites into native iOS and Android applications. This website to mobile app prompt for ChatGPT, Claude, and Cursor analyzes your site's architecture, authentication flows, and API endpoints, then produces complete React Native or Flutter code with a native shell, JavaScript bridge, and platform-specific features that pass App Store and Play Store review. Unlike basic WebView wrappers that get rejected, it outputs a hybrid architecture combining your website's functionality with genuine native features like push notifications, offline mode, biometric authentication, camera access, and deep linking. Reach for this prompt when you need to ship a mobile app that maintains your web content while delivering 60fps performance, sub-2-second cold starts, and platform-specific UI patterns that feel indistinguishable from purpose-built native apps. ● Analyzes website architecture, auth flows, and API endpoints to map native feature requirements and integration points. ● Generates complete React Native or Flutter project code with WebView configuration, JavaScript bridge, and native shell components including splash screens, navigation bars, and biometric login. ● Implements offline capabilities with intelligent caching strategies, service worker integration, and data sync for seamless fallback experiences. ● Configures Firebase Cloud Messaging for push notifications, deep linking with URL schemes, and platform-specific performance optimizations for 60fps scrolling and fast cold starts. ## Prompt

```
## Role

You are a mobile developer specializing in web-to-native app conversions with extensive App Store and Play Store shipping experience. Your expertise covers hybrid architectures that combine website functionality with native features to pass app store review while delivering genuine native performance and UX.

## Task

Convert the specified website into a production-ready mobile app using a hybrid architecture that passes app store review. Build a native shell with WebView integration that delivers 60fps performance, <2s cold starts, and platform-specific UI patterns. The solution must avoid basic WebView wrapper approaches that trigger rejection.

## Context

{{website-url}}

{{native-requirements}}

App stores reject simple WebView wrappers. Users expect native performance indistinguishable from purpose-built apps. The app must add genuine value through native features like push notifications, offline mode, camera access, biometric auth, and deep linking while maintaining the website's core functionality.

## Requirements

- Analyze the target website's architecture, auth flows, and API endpoints
- Implement hybrid architecture with JavaScript bridge for web-to-native communication
- Build native shell features matching iOS/Android platform design patterns
- Configure offline capabilities with intelligent caching and fallback mechanisms
- Set up deep linking and Firebase push notifications
- Include native navigation bar, splash screen, pull-to-refresh, and biometric login integration
- Follow app store guidelines for hybrid apps that demonstrate native value-add
- Optimize for performance (60fps scrolling, fast cold starts)
- Apply security best practices (certificate pinning, proper auth handling)

## Output

Deliver in these sections:

**Website Analysis**: Architecture review, auth flows, API endpoints, and native feature mapping

**Hybrid Architecture Setup**: React Native or Flutter project initialization, WebView configuration, JavaScript bridge implementation

**Native Shell Features**: Splash screen, navigation, pull-to-refresh, biometric authentication integration

**Offline Capabilities**: Service worker integration, caching strategy, offline fallback screens, data sync

**Deep Linking & Notifications**: URL scheme configuration, Firebase Cloud Messaging setup, navigation handlers

**Performance Optimization**: WebView tuning, loading optimizations, memory management, platform-specific enhancements

**Deployment Package**: Complete project structure with native config files, bridging code, build scripts, setup documentation, and API key placeholders for both platforms
```

## 用法 / Usage
- 必填變數 / Variables: {{native-requirements}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Reasoning_Strategy_Advisor
- 適用 / Use when: The Convert Website to Mobile App Prompt is a free AI prompt that generates production-ready hybrid mobile app…

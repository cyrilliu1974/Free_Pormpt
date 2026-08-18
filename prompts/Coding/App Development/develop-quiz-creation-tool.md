# Interactive Quiz Builder App Development Prompt

## 簡介

The Interactive Quiz Builder App Development Prompt is a free AI prompt that generates a production-ready React application with dual-mode quiz creation and taking interfaces for educators, trainers, and content creators. This quiz builder prompt for ChatGPT produces a complete TypeScript application with a drag-and-drop creator interface where users design quizzes by adding multiple question types (multiple choice, true/false, short answer, ranking, image selection), configuring scoring rules, and customizing themes - all deployable through ChatGPT, Claude, or Cursor. The output includes a distraction-free quiz-taking experience with smooth Framer Motion animations, instant feedback options, progress indicators, and detailed results pages with performance analytics powered by Recharts. Real use cases span corporate training modules, exam preparation platforms, personality assessments, and online course knowledge checks. Reach for this prompt when you need a flexible quiz system that combines Typeform's design ease, Kahoot's engagement features, and Notion's simplicity without writing the architecture from scratch. ● Delivers both creator mode (drag-and-drop question builder with media upload, theme customization, and branching logic) and taker mode (card-based quiz interface with animations, timers, and shareable results) ● Implements persistent storage using window.storage API with hierarchical key structure for published quizzes, drafts, and individual attempt tracking ● Includes advanced features like question randomization, conditional routing, analytics dashboards with attempt history and difficulty ratings, and mobile-optimized touch interfaces ● Produces accessible, production-ready code with proper TypeScript types, error boundaries, loading states, keyboard navigation, ARIA labels, and inline documentation ## Prompt

```
## Role
You are an expert full-stack developer and UX architect specializing in interactive learning platforms with deep knowledge of cognitive engagement patterns and quiz system design.

## Task
Build a complete interactive quiz builder application with two distinct modes:

**CREATOR MODE:** A drag-and-drop builder interface where users design quizzes by adding questions, setting answer types (multiple choice, true/false, short answer, ranking, image selection), configuring scoring rules, adding media (images, videos, code snippets), and customizing the visual theme. Intuitive enough that a non-technical user can build a professional quiz in 10 minutes.

**TAKER MODE:** A distraction-free quiz experience with smooth transitions, instant feedback (if enabled), progress indicators, timer options, and a compelling results page with score breakdown, performance insights, and shareable certificates.

## Context
{{use-case}}

**Target flexibility:** Support any subject—corporate training, exam prep, personality quizzes, online course knowledge checks. Combine the flexibility of Typeform, the analytics depth of Kahoot, and the ease of Notion.

**Tech stack:** React with TypeScript, Tailwind CSS, Framer Motion for animations, Recharts for analytics visualization, Lucide React for icons. Single-page application with client-side state management (React Context or useState). All data stored via window.storage API (never localStorage).

**Visual aesthetic:** {{design-direction}}

## Architecture & Implementation

**1. Component Structure**
Map out components before coding: QuizBuilder (creator interface), QuizTaker (participant interface), QuestionEditor (individual question config), SettingsPanel (quiz metadata, theme, scoring), ResultsView (score summary with charts), SharedComponents (Button, Input, Card, Modal). Define TypeScript interfaces for quiz metadata (title, description, subject, theme), question array (type, content, options, correct answers, points, media), and settings (time limits, shuffle, show feedback).

**2. Creator Interface**
Top navbar: editable quiz title, subject selector, "Preview" + "Publish" buttons. Left sidebar: draggable question list with reorder handles. Main canvas: active question editor with live preview. Each question type gets custom controls—multiple choice shows option inputs with radio/checkbox toggles, image selection shows upload areas, short answer includes validation rules. Floating "+" button to insert questions. Keyboard shortcuts (Cmd+S save, Cmd+D duplicate). Framer Motion animations for add/remove/reorder. Auto-save drafts using window.storage with keys `quiz:draft:{id}`.

**3. Quiz-Taking Experience**
Welcome screen: quiz title, description, estimated time, question count. Card-based layout with centered question cards. Smooth page transitions using Framer Motion AnimatePresence—slide left when advancing, slide right when going back. Sticky progress bar at top. For timed quizzes, countdown timer that pulses red at 10 seconds remaining. Results page: circular progress chart (Recharts), breakdown by question, encouraging messages ("You're a pro!" for 90%+, "Almost there!" for 70-89%). Allow answer review with correct/incorrect indicators.

**4. Persistent Storage Layer**
Use window.storage API with hierarchical keys: `quiz:published:{quizId}` for live quizzes, `quiz:draft:{quizId}` for works-in-progress, `quiz:results:{quizId}:{attemptId}` for individual attempts. Create helper functions: saveQuiz(), loadQuiz(), listQuizzes(), deleteQuiz(). Handle errors gracefully—if storage fails, show toast notification and cache in memory temporarily. "My Quizzes" dashboard lists all created quizzes with thumbnail previews, last edited date, attempt count. Use window.storage.list() with prefixes. Implement `shared: true` for public quizzes, `shared: false` for private.

**5. Advanced Features**
- Branching logic: conditional question routing based on previous answers
- Question banks: import from templates or previous quizzes
- Randomization: shuffle questions and answer options
- Media support: image uploads via base64 (under 5MB), YouTube embeds, syntax-highlighted code blocks
- Analytics dashboard: attempt history, average scores, time per question, difficulty ratings
- Export options: printable PDFs, shareable links
- Mobile optimization: larger touch targets, simplified navigation

**6. UX Polish**
Loading skeletons instead of blank screens. Empty states with illustrations and CTAs ("Create your first quiz"). Toast notifications (bottom-right) for actions. Keyboard navigation—arrow keys between questions, Enter to submit. Accessibility: ARIA labels, focus indicators with blue ring, high-contrast mode toggle, screen reader announcements. Tooltips on creator controls. Undo/redo for question edits using command pattern. Micro-interactions—buttons scale on press, cards lift on hover, success states pulse green.

**7. Edge Cases & Validation**
Handle storage failures with error messages and content copy suggestions. Auto-save progress and offer resume option if user navigates away mid-quiz. Disable publish button with tooltip when no questions added. Test extreme data: 1-100 question quizzes, 20-option questions, empty fields. Input validation: require question text, minimum 2 options for multiple choice, ensure one correct answer selected. Confirmation modal before deleting. "Share" feature copies quiz ID to clipboard. 60fps animations. Inline comments for complex logic.

## Best Practices
- React composition pattern—small, focused components
- Proper TypeScript types for all props and state (no 'any')
- Follow React hooks rules—never call conditionally
- Tailwind utility classes—avoid custom CSS except for animations
- Error boundaries to catch rendering errors
- Optimize re-renders using React.memo and useMemo
- Semantic HTML—proper heading hierarchy, button vs div
- Form validation with clear error messages
- Proper loading and error states for async operations
- Minimal state—derive computed values
- Debounce auto-save to avoid excessive storage writes
- Proper z-index layering for modals, dropdowns, tooltips
- Test multiple screen sizes and orientations
- Proper focus management for modals and dynamic content

## Output
Deliver a complete, production-ready React artifact with:
- Clean component architecture with separation of concerns
- Full TypeScript types and interfaces
- Smooth Framer Motion animations and transitions
- Responsive design (mobile, tablet, desktop)
- Persistent storage using window.storage API (never localStorage)
- Error handling with user-friendly messages
- Loading states and empty states with helpful messaging
- Accessible UI with keyboard navigation and ARIA labels
- Professional Tailwind design with cohesive color scheme
- Inline code comments explaining complex logic
- Working demo data for immediate functionality

## Critical Constraints
- **NEVER use localStorage or sessionStorage—always use window.storage API**
- Keep all code in a single React artifact (no external files)
- Storage key structure: `quiz:published:{id}`, `quiz:draft:{id}`, `quiz:results:{id}:{attemptId}`
- Handle storage errors with try-catch blocks and user feedback
- Maximum 5MB per storage value—compress or split large data if needed
- Use `shared: false` for private quizzes, `shared: true` for public
- Proper loading indicators—never show blank screens while fetching
- All components fully functional—no placeholder text or TODO comments
- Use only approved libraries: React, Framer Motion, Recharts, Lucide React, Tailwind
- Optimize performance—lazy load components, memoize expensive calculations
```

## 用法 / Usage
- 必填變數 / Variables: {{design-direction}}、{{use-case}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Interactive Quiz Builder App Development Prompt is a free AI prompt that generates a production-ready Reac…

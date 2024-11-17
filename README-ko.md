# TkEasyGUI

`TkEasyGUI`는 Python에서 GUI를 가장 쉽게 작성할 수 있는 라이브러리입니다.

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/logo-button.jpg" width="180" alt="TkEasyGUI 로고">

- Python 표준 UI 라이브러리인 `Tkinter`는 종종 접근 장벽이 높고 사용하기 어렵다고 여겨집니다. 이 라이브러리를 사용하면 GUI 애플리케이션을 쉽고 직관적으로 만들 수 있습니다.
- 이벤트 모델은 잘 알려진 GUI 라이브러리인 `PySimpleGUI`와 호환됩니다.
- 이 패키지는 타입 힌트를 지원하여 코드 완성을 통해 속성을 선택할 수 있습니다. `Python 3.9 이상`이 필요합니다.
- 이 프로젝트는 관대한 MIT 라이선스를 채택하고 있으며, 이 라이선스는 향후 변경되지 않을 것입니다. 함께 GUI 프로그램 제작을 즐겨보세요.

- [👉日本語](https://github.com/kujirahand/tkeasygui-python/blob/main/README-ja.md) / [👉中文](https://github.com/kujirahand/tkeasygui-python/blob/main/README-zh.md)

> This document has been translated automatically. Please let us know if you find any unnatural expressions.

## 플랫폼

- Windows / macOS / Linux (Tkinter 필요)

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/tkeasygui-shot640.jpg" width="300" alt="TkEasyGUI">

## 설치

[PyPI](https://pypi.org/project/TkEasyGUI/)에서 패키지 설치:

```sh
pip install TkEasyGUI
# 또는
python -m pip install TkEasyGUI
```

[GitHub Repository](https://github.com/kujirahand/tkeasygui-python)에서 패키지 설치:

```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

- (메모) 0.2.24 이전 버전에서 업데이트 시 실패할 수 있습니다. ([해결 방법 보기](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/installation_trouble.md))

## 사용 방법 - 팝업 대화상자

TkEasyGUI를 사용하는 것은 간단합니다. 대화상자만 표시하려면 두 줄의 코드만 필요합니다.

```py
import TkEasyGUI as eg
# 텍스트 대화상자 표시
eg.print("기쁨의 마음은 좋은 약이다.")
```

사용자에게 이름을 묻고 창에 이름을 표시합니다.

```py
import TkEasyGUI as eg
# 입력 대화상자 표시
name = eg.input("당신의 이름은 무엇인가요?")
eg.print(f"안녕하세요, {name}님.")
```

또한, 여러 입력 필드를 지정할 수 있는 대화상자도 사용할 수 있습니다.

```py
import TkEasyGUI as eg
# 폼 대화상자 표시
form = eg.popup_get_form(["이름", "나이", "취미"])
if form:
    name = form["이름"]
    age = form["나이"]
    hobbies = form["취미"]
    eg.print(f"이름={name}, 나이={age}, 취미={hobbies}")
```

- [문서 > 대화상자](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/dialogs-py.md)


### 사용 방법 - 위젯

레이블과 버튼만 있는 간단한 창을 생성하려면 다음과 같이 작성할 수 있습니다.

```py
import TkEasyGUI as eg
# 레이아웃 정의
layout = [
    [eg.Text("안녕하세요, 세상!")],
    [eg.Button("확인")]
]
# 창 생성
with eg.Window("Hello App", layout) as window:
    # 이벤트 루프
    for event, values in window.event_iter():
        if event == "확인":
            eg.print("감사합니다.")
            break
```

PySimpleGUI와 유사한 이벤트 모델을 사용하여 설명할 수 있습니다.

```py
import TkEasyGUI as eg

# 레이아웃 정의
layout = [[eg.Text("안녕하세요, 세상!")], [eg.Button("확인")]]
# 창 생성
window = eg.Window("Hello App", layout)
# 이벤트 루프
while True:
    event, values = window.read()
    if event in ["확인", eg.WINDOW_CLOSED]:
        eg.popup("감사합니다.")
        break
# 창 닫기
window.close()
```

- [문서 > 사용할 수 있는 요소는?](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/README.md#tkeasygui-elements-list)

## 샘플

간단한 사용 방법을 보여주는 여러 샘플을 준비했습니다. 확인해 보세요.

- [샘플](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

`tests/file_viewer.py`를 실행하면 모든 샘플을 쉽게 실행할 수 있습니다.

## 문서

다음은 클래스와 메서드의 상세 목록입니다.

- [문서](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)
  - [대화상자](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/dialogs-py.md)
  - [요소](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/widgets-py.md)
  - [유틸리티](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/utils-py.md)

## 튜토리얼

일본어 튜토리얼:

- [TkEasyGUI - Python으로 가장 빠르게 데스크톱 애플리케이션을 만드는 라이브러리](https://note.com/kujirahand/n/n33a2df3aa3e5)
- [마이나비 뉴스 Python 연재 116회 - 합계/서식/복사 도구 만들기](https://news.mynavi.jp/techplus/article/zeropython-116/)
- [(도서) Python으로 만드는 데스크톱 앱 메모장부터 스크레이핑 및 생성 AI 활용까지](https://amzn.to/45R2NSH)

## PySimpleGUI와의 호환성

- 기본 기능을 사용할 때 PySimpleGUI와 호환됩니다. PySimpleGUI와 동일한 이벤트 구동 모델을 사용하여 프로그램을 작성할 수 있습니다.  
- 기본 GUI 구성 요소의 이름은 동일하게 유지되지만, 일부 속성 이름은 다릅니다.  
- TkEasyGUI는 완전히 새로 구현되었으며 MIT 라이선스 하에 제공됩니다.
- 그러나 PySimpleGUI와의 완전한 호환성을 목표로 하지는 않습니다.

### TkEasyGUI의 주요 기능:

- `for` 루프와 `window.event_iter()`를 사용하여 간단한 이벤트 처리가 가능합니다.
- 색상 선택 대화상자(`eg.popup_color`), 폼 대화상자(`eg.popup_get_form`) 등 맞춤형 팝업 대화상자가 제공됩니다.
- `Image` 클래스는 PNG뿐만 아니라 JPEG 형식도 지원합니다.
- 대량 이벤트 등록을 위한 편리한 이벤트 훅 및 기능 제공 - [docs/custom_events](docs/custom_events.md).
- 텍스트 박스(Multiline/Input)에 복사, 붙여넣기, 잘라내기 기능이 추가되었습니다.
- 시스템의 기본 색상 스킴을 활용합니다.

## 링크

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)
- [Discord > TkEasyGUI](https://discord.gg/G2JXaRft)
- 
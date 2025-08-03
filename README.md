# 🎲 로또 번호 생성기 v1.0
<img src="https://github.com/user-attachments/assets/ca345898-8b6f-4a0d-bee2-847a02ffc0eb" width="40%" height="40%" alt="로또 번호 생성기 v1.0" />

## 💻 개발자 소개
|김서원|
|:---:| 
|<a href="https://github.com/CALKO9611"><img src="https://avatars.githubusercontent.com/u/89835647?v=4" width="150"/></a>|
|BLOG : [CALKO LAB](https://calkolab.tistory.com/) |

## 📄 프로젝트 소개
간단하고 직관적인 **로또 번호 생성기 데스크탑 앱**입니다.  
버튼 클릭 한 번으로 로또 번호 조합(6개 숫자)을 생성할 수 있습니다.
또한 `동행복권 API`를 사용하여 최근 회차 번호 자동으로 계산하여 출력해 줍니다.

이 프로젝트는 Python의 GUI 라이브러리인 **Tkinter**로 제작되었으며, `로또 번호 생성기 v1.0.exe` 실행 파일로 배포되어 별도의 Python 설치 없이도 누구나 사용할 수 있습니다.

## 🎨 디자인 초안
<img src="https://github.com/user-attachments/assets/09bf0a93-449c-49a2-91a2-b3eae99701d1" width="40%" height="40%" alt="디자인 초안">

## ✅ 주요 기능
- 중복 없는 로또 번호(1~45) 6개 자동 생성
- 직관적인 GUI
- 별도의 설치 과정 없이 바로 실행 가능한 .exe 배포

## 🖱️ 실행 방법
1. `로또 번호 생성기 v1.0.exe` 파일을 실행합니다.
2. `게임 수`를 설정한 뒤 `시작` 버튼을 클릭합니다.

## 🛠️ 기술 스택
- **Python 3.13**
- **Tkinter** - GUI 인터페이스 구성
- **PyInstaller** – `.exe` 배포 파일 생성

## 📁 파일 구조
`Lotto_Number_Generator`/  
├── `app.py`　　　　　　　　　　# Title 및 Tkinter 실행  
├── `layout.py`　　　　　　　　# UI 꾸미기  
├── `lotto_logic.py`　　　　　　# 메인 로직  
├── `icon32.ico`　　　　　　　　# 아이콘  
├── `.gitignore`  
├── `.prettierignore`  
├── `로또 번호 생성기 v1.0.exe` # 실행 파일  
└── `README.md`  


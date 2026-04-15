# 프로젝트 개요

개발 환경을 구축하고 개발 및 배포 환경에 대한 기초를 익힌다.

- 체크리스트: [CHECKLISTS.md](CHECKLISTS.md)
- 작업 로그: [LOGS.md](LOGS.md)

# 실행 환경

- Docker version 28.5.2, build ecc6942
- git version 2.53.0
- macOS Sequoia Version 15.7.4 (24G517)
- zsh 5.9 (x86_64-apple-darwin24.0)

# 정리한 내용

## 파일 관리 명령어

- cd <dir>: change directory, 디렉토리 이동
- mv <source> <dest>: move, 특정 파일이나 폴더를 dest로 이동. 파일 이름 변경에도 사용됨
- rm <target>: remove, 대상 파일 제거. 
- rmdir <target>: remove directory, 대상 폴더 제거. 대상 폴더가 비어있을 때에만 제거 가능
- rm -rf <target>: target directory와 그 안의 모든 내용을 삭제. `r`, `f`는 각각 recursive(재귀적으로), force(존재하지 않는 파일이나 권한 오류 무시, 확인 프롬프트 생략)를 뜻한다.

## 권한 관련 명령어

- chmod <mode> <target>: change mode, 파일/디렉토리의 접근 권한 변경. 숫자(8진수) 또는 기호(u/g/o + r/w/x) 방식으로 지정

  ### 기호 방식

  대상 기호: `u`(user, 소유자), `g`(group, 그룹), `o`(others, 기타), `a`(all, 전체)  
  연산자: `+`(권한 추가), `-`(권한 제거), `=`(권한 지정)  
  권한 기호: `r`(read), `w`(write), `x`(execute)

  | 예시 | 설명 |
  |------|------|
  | `u+r` | 소유자에게 읽기 권한 추가 |
  | `u+x` | 소유자에게 실행 권한 추가 |
  | `o+w` | 기타 사용자에게 쓰기 권한 추가 |
  | `o-w` | 기타 사용자의 쓰기 권한 제거 |
  | `g=rx` | 그룹의 권한을 읽기+실행으로 지정 |
  | `a+x` | 모든 사용자에게 실행 권한 추가 |

  ### 8진수 방식

  `r=4`, `w=2`, `x=1`로 대응하며, 세 자리 숫자로 `소유자/그룹/기타` 권한을 한 번에 지정한다.

  | 숫자 | 이진수 | 권한 |
  |------|--------|------|
  | 7 | 111 | rwx |
  | 6 | 110 | rw- |
  | 5 | 101 | r-x |
  | 4 | 100 | r-- |
  | 0 | 000 | --- |

  예시: `chmod 754 file`
  - `7` (소유자): rwx
  - `5` (그룹): r-x
  - `4` (기타): r--

  ### 권한 문자열 해석 (`ls -l` 출력)

  예시: `-rwxr-xr--`

  | 위치 | 문자 | 의미 |
  |------|------|------|
  | 1번째 | `-` | 파일 종류 (`-`: 일반 파일, `d`: 디렉토리, `l`: 심볼릭 링크) |
  | 2~4번째 | `rwx` | 소유자 권한: 읽기+쓰기+실행 |
  | 5~7번째 | `r-x` | 그룹 권한: 읽기+실행 |
  | 8~10번째 | `r--` | 기타 권한: 읽기만 |

- chown <user>:<group> <target>: change owner, 파일/디렉토리의 소유자 및 그룹 변경
- chgrp <group> <target>: change group, 파일/디렉토리의 그룹 변경
- ls -l: 파일 목록을 권한 정보와 함께 출력. 첫 번째 컬럼(예: `-rwxr-xr--`)에서 권한 확인 가능


## Docker 관련 정리

Docker는 컨테이너 가상화 도구로, 일관된 환경에서 애플리케이션이 동작할 수 있도록 namespace/cgroups 등의 기술을 이용하여 호스트와 격리된 환경을 제공한다.
하나의 격리된 환경을 컨테이너라 하고, 이 컨테이너를 만들 수 있는 템플릿을 이미지라 한다.
이미지에는 원하는 컨테이너를 실행할 때 필요한 모듈과 정보를 담을 수 있으며, Dockerfile을 빌드하여 만들 수 있다.

하이퍼바이저 가상화와 다른 점은, 하이퍼바이저 가상화는 가상화 계층 위에 Guest OS 자체를 올리지만 컨테이너 가상화는 컨테이너가 OS의 커널 API를 직접 끌어다 쓴다는 점이다. 

추가) 대부분의 이미지는 Linux OS기반이기 때문에, Windows에서 도커 컨테이너를 실행하려면 WSL2 위에 리눅스 커널을 띄우고, 그 위에 컨테이너를 띄워야 한다. 하이퍼바이저 가상화를 하고 그 위에서 컨테이너 가상화를 하는거라, 윈도우에서 도커로 뭔가 하려고 한다면 그것은 막심한 손해다.

이미지와 컨테이너는 각각 `읽기 전용 파일 시스템 레이어`의 집합이다. 쉽게 말해 설계도 같은 것이다. 애플리케이션의 실행에 필요한 파일을 읽기 전용으로 모아둔 것이다.

컨테이너는 이미지에 r/w layer를 추가한 인스턴스이다. 컨테이너 내에서 발생하는 모든 파일 변경은 이 writable r/w layer에 기록된다.

### 이미지 관련

- `docker pull <image>`: Docker Hub에서 이미지 다운로드
- `docker images`: 로컬에 저장된 이미지 목록 확인
- `docker rmi <image>`: 이미지 삭제
- `docker build -t <name>:<tag> <path>`: Dockerfile로 이미지 빌드. `-t`는 생략 가능하나, 생략 시 관리하기가 매우 불편하다. path는 context root로, 관례상 Dockerfile이 위치한 곳을 기준으로 루트를 잡는다.

### 컨테이너 실행 및 관리

- `docker run <image>`: 이미지로 컨테이너 생성 및 실행
  - `-d`: 백그라운드(detached) 모드로 실행
  - `-it`: 인터랙티브 터미널로 실행 (`-i` + `-t`)
  - `--name <name>`: 컨테이너 이름 지정
  - `-p <host_port>:<container_port>`: 포트 포워딩
  - `-v <host_path>:<container_path>`: 볼륨 마운트
  - `--rm`: 컨테이너 종료 시 자동 삭제
- `docker start <container>`: 중지된 컨테이너 시작
- `docker stop <container>`: 실행 중인 컨테이너 중지
- `docker rm <container>`: 컨테이너 삭제

### 컨테이너 상태 확인

- `docker ps`: 실행 중인 컨테이너 목록
- `docker ps -a`: 모든 컨테이너 목록 (중지된 것 포함)
- `docker logs <container>`: 컨테이너 로그 출력
- `docker inspect <container>`: 컨테이너 상세 정보 출력

### 컨테이너 내부 접근

- `docker exec -it <container> <command>`: 실행 중인 컨테이너에 명령 실행
  - 예시: `docker exec -it mycontainer /bin/bash` — bash 셸로 진입


## Dockerfile 문법

- `FROM <image>:<tag>`: 베이스 이미지 지정. 다른 이미지를 기반으로 커스텀 이미지를 만들 때 사용함. Dockerfile의 첫 번째 명령어여야 함
  - 예시: `FROM ubuntu:22.04`
- `RUN <command>`: 이미지 빌드 시 실행할 명령어. 레이어를 생성함
  - 예시: `RUN apt-get update && apt-get install -y curl`
- `CMD ["executable", "arg1"]`: 컨테이너 시작 시 실행할 기본 명령. `docker run`에서 명령을 지정하면 덮어씌워짐
- `ENTRYPOINT ["executable", "arg1"]`: 컨테이너 시작 시 항상 실행할 명령. `docker run`으로 덮어씌울 수 없음
- `COPY <src> <dest>`: 호스트의 파일/디렉토리를 이미지 안으로 복사
- `ADD <src> <dest>`: `COPY`와 유사하나 URL 다운로드, tar 자동 압축 해제 기능 추가. 단순 복사는 `COPY`사용이 권장됨
- `WORKDIR <path>`: 이후 명령어의 작업 디렉토리 설정. 없으면 자동 생성
- `ENV <key>=<value>`: 환경변수 설정. 빌드 및 컨테이너 실행 시 모두 적용
- `ARG <name>=<default>`: 빌드 시에만 사용하는 변수. `docker build --build-arg`로 값 전달 가능
- `EXPOSE <port>`: 컨테이너가 사용할 포트를 문서화. 실제 포트 개방은 `docker run -p`로 해야 함
- `VOLUME <path>`: 컨테이너의 특정 경로를 볼륨으로 지정
- `USER <user>`: 이후 명령어를 실행할 사용자 지정

주의) .env 파일이나 을 도커 이미지에 포함시킬 경우 Docker hub등에 배포할 때 .env가 노출될 수 있으므로, COPY 등의 명령에서
환경변수 파일을 복사하지 않도록 .dockerignore에 추가해둬야 한다.

### 볼륨 관리

볼륨은 `docker run` 시 자동 생성되므로 반드시 미리 만들 필요는 없다. 단, `docker volume create`로 명시적으로 생성하면 드라이버나 옵션을 지정할 수 있다.

- `docker volume create <name>`: 볼륨 생성. 경로는 호스트 머신의 도커 엔진이 자동 관리하고, 컨테이너를 실행할 때 해당 볼륨명을 통해 접근 가능하다.
- `docker volume ls`: 볼륨 목록 확인
- `docker volume inspect <name>`: 볼륨 상세 정보 출력 (마운트 경로, 드라이버 등)
- `docker volume rm <name>`: 볼륨 삭제 (연결된 컨테이너가 없어야 함)
- `docker volume prune`: 컨테이너에 연결되지 않은 볼륨 전체 삭제

볼륨을 컨테이너에 연결하는 방법은 두 가지다.

| 방식 | 예시 | 설명 |
|------|------|------|
| `-v` (단축 문법) | `-v myvolume:/app/data` | named volume 연결 |
| `-v` (bind mount) | `-v /host/path:/container/path` | 호스트 경로를 직접 마운트 |
| `--mount` (명시적 문법) | `--mount type=volume,src=myvolume,dst=/app/data` | 옵션을 명시적으로 지정 |

`-v`로 named volume을 지정할 때 해당 볼륨이 없으면 Docker가 자동으로 생성한다.  
`--mount`는 볼륨이 없으면 에러를 내기 때문에, 자동 생성을 원하지 않을 때 더 안전하다.

## 포트 매핑 및 볼륨이 필요한 이유

| Reference: https://docs.docker.com/engine/storage/volumes

기본적으로 도커는 writable layer 위에서 작동한다. 따라서 컨테이너를 실행하면, 컨테이너 내부 앱에서 파생된 모든 파일들은 writable layer에 쓰여진다.

하지만 이 writable layer은 도커 컨테이너가 제거될 경우 함께 제거되기 때문에 추적이 매우 어렵고, 호스트 머신에서 직접 액세스하려면 컨테이너의 쉘을 통해 액세스해야하는 불편함이 있다.

그리고 이 writable layer에 파일을 쓰려면 파일시스템을 관리해주는 추가 레이어를 거쳐야 하는데, 이 부분이 큰 병목이 될 수 있다. volume을 직접 지정할 경우 다른 커널 API처럼 호스트의 파일 시스템에 직접 접근하기 때문에 더 빠르다.

포트 매핑은 서로 다른 컨테이너에서 같은 애플리케이션을 돌리더라도, 애플리케이션에 맞는 상용 포트를 그대로 사용할 수 있다는 점에서 매우 큰 장점을 갖는다.

예를 들어, ssl이 적용된 nginx서버는 내부적으로 443번 포트를 사용하도록 할 수 있고, 여러 개의 nginx ssl 컨테이너를 돌리더라도 컨테이너 내부에서나 컨테이너끼리 통신할 때에는 443번 포트를 그대로 이용할 수 있다.

물론 외부에 모든 컨테이너의 포트를 노출해야 한다면 포트 매핑은 큰 장점이 아닐 수 있다. 어차피 호스트에서 포트 번호를 관리해야 하기 때문이다.

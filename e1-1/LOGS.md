# 수행 로그

## 1. 터미널 조작 로그

### 1-1. 현재 위치 확인

```bash
pwd
```

```bash
/Users/cla6shade8560
```

### 1-2. 목록 확인(숨김 파일 포함)

```bash
ls -al
```

```bash
total 8
drwxr-x---+ 18 cla6shade8560  cla6shade8560   576 Apr  5 14:49 .
drwxr-xr-x  10 root           admin           320 Apr  5 14:07 ..
-r--------   1 cla6shade8560  cla6shade8560     7 Apr  5 14:07 .CFUserTextEncoding
drwx------+  2 cla6shade8560  cla6shade8560    64 Apr  5 14:07 .Trash
drwxr-xr-x   5 cla6shade8560  cla6shade8560   160 Apr  5 14:07 .docker
drwxr-xr-x  10 cla6shade8560  cla6shade8560   320 Apr  5 14:07 .orbstack
drwxr-xr-x   3 cla6shade8560  cla6shade8560    96 Apr  5 14:07 .ssh
drwxr-xr-x   3 cla6shade8560  cla6shade8560    96 Apr  5 14:07 .vscode
drwx------   3 cla6shade8560  cla6shade8560    96 Apr  5 14:49 .zsh_sessions
drwx------+  3 cla6shade8560  cla6shade8560    96 Apr  5 14:07 Desktop
drwx------+  3 cla6shade8560  cla6shade8560    96 Apr  5 14:07 Documents
drwx------+  3 cla6shade8560  cla6shade8560    96 Apr  5 14:07 Downloads
drwx------@ 78 cla6shade8560  cla6shade8560  2496 Apr  5 15:14 Library
drwx------   3 cla6shade8560  cla6shade8560    96 Apr  5 14:07 Movies
drwx------+  3 cla6shade8560  cla6shade8560    96 Apr  5 14:07 Music
drwx------   4 cla6shade8560  cla6shade8560   160 Apr  5 14:07 OrbStack
drwx------+  4 cla6shade8560  cla6shade8560   128 Apr  5 14:07 Pictures
drwxr-xr-x+  4 cla6shade8560  cla6shade8560   128 Apr  5 14:07 Public
```

### 1-3. 이동

```bash
cd Public
```

```bash
cla6shade8560@c4r4s7 Public %  
```

### 1-4. 생성

폴더 생성

```bash
mkdir projects
```

```bash
cla6shade8560@c4r4s7 ~ % ls
Desktop		Downloads	Movies		OrbStack	Public
Documents	Library		Music		Pictures	projects
```

파일 생성

```bash
touch example.txt
```

```bash
cla6shade8560@c4r4s7 projects % ls
example.txt
```

### 1-5. 복사

```bash
cp example.txt example-cp.txt
```

```bash
cla6shade8560@c4r4s7 projects % ls
example-cp.txt	example.txt
```

### 1-6. 이동/이름변경

```bash
mv example.txt example-rename.txt
```

```bash
cla6shade8560@c4r4s7 projects % ls
example-rename.txt
```

### 1-7. 삭제

```bash
rm example.txt
```

```bash
cla6shade8560@c4r4s7 projects % ls
example-cp.txt 
```

### 1-8. 파일 내용 확인

```bash
cat example.txt
```

*(출력 없음)*

## 2. 권한 실습 및 증거 기록

폴더

```bash
cla6shade8560@c4r4s7 ~ % ls -al
drwxr-xr-x   2 cla6shade8560  cla6shade8560    64 Apr  5 15:33 projects
```

```bash
chmod 777 projects
```

```bash
cla6shade8560@c4r4s7 ~ % ls -al
drwxrwxrwx   2 cla6shade8560  cla6shade8560    64 Apr  5 15:33 projects
```

파일

```bash
cla6shade8560@c4r4s7 ~ % ls -al
-rw-r--r--   1 cla6shade8560  cla6shade8560    0 Apr  5 15:38 example.txt
```

```bash
chmod 777 example.txt
```

```bash
cla6shade8560@c4r4s7 ~ % ls -al
-rwxrwxrwx   1 cla6shade8560  cla6shade8560    0 Apr  5 15:38 example.txt
```

## 3. Docker 설치 및 기본 점검

### 3-1. Docker 버전 확인

```bash
docker --version
```

```bash
Docker version 28.5.2, build ecc6942
```

## 3-2. Docker 데몬 동작 여부

```bash
docker info
```

```bash
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/cla6shade8560/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/cla6shade8560/.docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 28.5.2
 Storage Driver: overlay2
  Backing Filesystem: btrfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: d842d7719497cc3b774fd71620278ac9e17710e0
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.17.8-orbstack-00308-g8f9c941121b1
 Operating System: OrbStack
 OSType: linux
 Architecture: x86_64
 CPUs: 6
 Total Memory: 15.67GiB
 Name: orbstack
 ID: be6514e4-99a8-4e4e-8755-01420dcf9b2d
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine
 Default Address Pools:
   Base: 192.168.97.0/24, Size: 24
   Base: 192.168.107.0/24, Size: 24
   Base: 192.168.117.0/24, Size: 24
   Base: 192.168.147.0/24, Size: 24
   Base: 192.168.148.0/24, Size: 24
   Base: 192.168.155.0/24, Size: 24
   Base: 192.168.156.0/24, Size: 24
   Base: 192.168.158.0/24, Size: 24
   Base: 192.168.163.0/24, Size: 24
   Base: 192.168.164.0/24, Size: 24
   Base: 192.168.165.0/24, Size: 24
   Base: 192.168.166.0/24, Size: 24
   Base: 192.168.167.0/24, Size: 24
   Base: 192.168.171.0/24, Size: 24
   Base: 192.168.172.0/24, Size: 24
   Base: 192.168.181.0/24, Size: 24
   Base: 192.168.183.0/24, Size: 24
   Base: 192.168.186.0/24, Size: 24
   Base: 192.168.207.0/24, Size: 24
   Base: 192.168.214.0/24, Size: 24
   Base: 192.168.215.0/24, Size: 24
   Base: 192.168.216.0/24, Size: 24
   Base: 192.168.223.0/24, Size: 24
   Base: 192.168.227.0/24, Size: 24
   Base: 192.168.228.0/24, Size: 24
   Base: 192.168.229.0/24, Size: 24
   Base: 192.168.237.0/24, Size: 24
   Base: 192.168.239.0/24, Size: 24
   Base: 192.168.242.0/24, Size: 24
   Base: 192.168.247.0/24, Size: 24
   Base: fd07:b51a:cc66:d000::/56, Size: 64

WARNING: DOCKER_INSECURE_NO_IPTABLES_RAW is set

```

## 4. Docker 기본 운영 명령 수행

### 4-1. 이미지 다운로드/목록 확인

```bash
docker images
```

```bash
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    e2ac70e7319a   13 days ago   10.1kB
ubuntu        latest    f794f40ddfff   5 weeks ago   78.1MB
```

### 4-2. 컨테이너 목록 확인

`-a` 옵션은 삭제된 컨테이너를 포함한 컨테이너 목록

```bash
docker ps
```

```bash
docker ps -a
```

```bash
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

### 4-3. 로그, 리소스 확인

(비고) docker 컨테이너가 없어 logs, stats로 조회 불가능 (6. 커스텀 이미지 제작에서 수행)

## 5. 컨테이너 실행 실습

### 5-1. hello-world 실행

```bash
docker pull hello-world && docker run hello-world
```

```bash
Using default tag: latest
latest: Pulling from library/hello-world
Digest: sha256:452a468a4bf985040037cb6d5392410206e47db9bf5b7278d281f94d1c2d0931
Status: Image is up to date for hello-world:latest
docker.io/library/hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### 5-2. ubuntu 컨테이너 실행

실행 후 즉시 연결 (interactive)

```bash
docker run -it ubuntu bash
```

```jsx
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
817807f3c64e: Pull complete 
Digest: sha256:186072bba1b2f436cbb91ef2567abca677337cfc786c86e107d25b7072feef0c
Status: Downloaded newer image for ubuntu:latest
root@0d7fe9229941:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@0d7fe9229941:/# cd ~
root@0d7fe9229941:~# ls
root@0d7fe9229941:~# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
root@0d7fe9229941:~# 
```

## 6~8. Dockerfile 기반 커스텀 이미지 제작 및 포트 매핑, 볼륨 지정

### 6-1. 이미지 빌드 및 컨테이너 실행/중지

```bash
docker build -t myapp:latest .
```

```bash
[+] Building 8.8s (7/7) FINISHED                                                                                            docker:orbstack
 => [internal] load build definition from Dockerfile                                                                                   0.2s
 => => transferring dockerfile: 88B                                                                                                    0.0s
 => [internal] load metadata for docker.io/library/nginx:latest                                                                        2.8s
 => [internal] load .dockerignore                                                                                                      0.1s
 => => transferring context: 2B                                                                                                        0.0s
 => [internal] load build context                                                                                                      0.2s
 => => transferring context: 3.92kB                                                                                                    0.0s
 => [1/2] FROM docker.io/library/nginx:latest@sha256:7150b3a39203cb5bee612ff4a9d18774f8c7caf6399d6e8985e97e28eb751c18                  4.6s
 => => resolve docker.io/library/nginx:latest@sha256:7150b3a39203cb5bee612ff4a9d18774f8c7caf6399d6e8985e97e28eb751c18                  0.2s
 => => sha256:7150b3a39203cb5bee612ff4a9d18774f8c7caf6399d6e8985e97e28eb751c18 10.23kB / 10.23kB                                       0.0s
 => => sha256:c3fe1eeae810f4a585961f17339c93f0fb1c7c8d5c02c9181814f52bdd51961c 2.29kB / 2.29kB                                         0.0s
 => => sha256:0cf1d6af5ca72e2ca196afdbdbe26d96f141bd3dc14d70210707cf89032ea217 9.09kB / 9.09kB                                         0.0s
 => => sha256:ec781dee3f4719c2ca0dd9e73cb1d4ed834ed1a406495eb6e44b6dfaad5d1f8f 29.78MB / 29.78MB                                       1.2s
 => => sha256:bb3d0aa29654655a18d97605cd63947d39ca5166d44c3341acc1bbc8d14a7a36 33.16MB / 33.16MB                                       1.2s
 => => sha256:510ddf6557d618d548b6f7680a84dfa925fea17316d335264eb3f09284850cd8 626B / 626B                                             1.0s
 => => sha256:cde7a05ae42831ee510e8948b80b25c297a1080875a3479c55a65f1e620fdb73 955B / 955B                                             1.5s
 => => extracting sha256:ec781dee3f4719c2ca0dd9e73cb1d4ed834ed1a406495eb6e44b6dfaad5d1f8f                                              1.1s
 => => sha256:587e3d84dbb5b5fc406b2b292318c9a446e72c144ad849b5ef8755f5037e8704 402B / 402B                                             1.7s
 => => sha256:3189680c601f46244f1706d0d197ddb415d9bb754236c042acffc76eeda37d39 1.21kB / 1.21kB                                         1.8s
 => => sha256:5e815e07e5699b40479214a6a2a30d647495d99cd0f253ee82f528f4814469ef 1.40kB / 1.40kB                                         2.1s
 => => extracting sha256:bb3d0aa29654655a18d97605cd63947d39ca5166d44c3341acc1bbc8d14a7a36                                              0.7s
 => => extracting sha256:510ddf6557d618d548b6f7680a84dfa925fea17316d335264eb3f09284850cd8                                              0.0s
 => => extracting sha256:cde7a05ae42831ee510e8948b80b25c297a1080875a3479c55a65f1e620fdb73                                              0.0s
 => => extracting sha256:587e3d84dbb5b5fc406b2b292318c9a446e72c144ad849b5ef8755f5037e8704                                              0.0s
 => => extracting sha256:3189680c601f46244f1706d0d197ddb415d9bb754236c042acffc76eeda37d39                                              0.0s
 => => extracting sha256:5e815e07e5699b40479214a6a2a30d647495d99cd0f253ee82f528f4814469ef                                              0.0s
 => [2/2] COPY nginx /usr/share/nginx/html                                                                                             0.4s
 => exporting to image                                                                                                                 0.2s
 => => exporting layers                                                                                                                0.1s
 => => writing image sha256:6eb9276c8c290eb54dd4295edc6ef7665e55066d3781dd6529e7493aaff71f85                                           0.0s
 => => naming to docker.io/library/myapp:latest      
```

```bash
docker run --rm -p 8080:80 -v ./volume:/var/log/nginx --name myapp myapp:latest
```

```bash
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
```

커스텀 포인트

- nginx/ 하위의 데모 페이지를 사용하도록 수정
- nginx 로그가 volume/내부에 쌓이도록 볼륨 지정
- 8080:80 매핑

```bash
docker stop myapp
```

```bash
myapp
```

### 6-2. stats/logs

```bash
docker stats
```

```bash
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS 
cf0d7d4b0655   myapp     0.00%     6.367MiB / 15.67GiB   0.04%     2.82kB / 5.01kB   16.8MB / 8.19kB   7 
```

```bash
docker logs
```

```bash
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
```

### 6-3. 컨테이너 삭제

```bash
docker rm myapp
```

```bash
myapp
```

### 6-4. 볼륨 생성

```bash
docker container create myappcontainer
```

```bash
myappcontainer
```

### 6-5. 컨테이너 삭제 전 데이터 확인 결과 기록

6-1에서 컨테이너 삭제 후에도, volume/error.log, volume/access.log는 존재했음. Docker container를 통한 프로세스 시작/종료 시에도 로그는 계속 보존됨.

- access.log
    
    ```bash
    2026/04/06 08:54:24 [notice] 1#1: using the "epoll" event method
    2026/04/06 08:54:24 [notice] 1#1: nginx/1.29.7
    2026/04/06 08:54:24 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
    2026/04/06 08:54:24 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
    2026/04/06 08:54:24 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
    2026/04/06 08:54:24 [notice] 1#1: start worker processes
    2026/04/06 08:54:24 [notice] 1#1: start worker process 29
    2026/04/06 08:54:24 [notice] 1#1: start worker process 30
    2026/04/06 08:54:24 [notice] 1#1: start worker process 31
    2026/04/06 08:54:24 [notice] 1#1: start worker process 32
    2026/04/06 08:54:24 [notice] 1#1: start worker process 33
    2026/04/06 08:54:24 [notice] 1#1: start worker process 34
    2026/04/06 09:01:34 [notice] 1#1: signal 3 (SIGQUIT) received, shutting down
    2026/04/06 09:01:34 [notice] 32#32: gracefully shutting down
    2026/04/06 09:01:34 [notice] 33#33: gracefully shutting down
    2026/04/06 09:01:34 [notice] 29#29: gracefully shutting down
    2026/04/06 09:01:34 [notice] 34#34: gracefully shutting down
    2026/04/06 09:01:34 [notice] 30#30: gracefully shutting down
    2026/04/06 09:01:34 [notice] 32#32: exiting
    2026/04/06 09:01:34 [notice] 33#33: exiting
    2026/04/06 09:01:34 [notice] 29#29: exiting
    2026/04/06 09:01:34 [notice] 34#34: exiting
    2026/04/06 09:01:34 [notice] 30#30: exiting
    2026/04/06 09:01:34 [notice] 33#33: exit
    2026/04/06 09:01:34 [notice] 32#32: exit
    2026/04/06 09:01:34 [notice] 34#34: exit
    2026/04/06 09:01:34 [notice] 29#29: exit
    2026/04/06 09:01:34 [notice] 30#30: exit
    2026/04/06 09:01:34 [notice] 31#31: gracefully shutting down
    2026/04/06 09:01:34 [notice] 31#31: exiting
    2026/04/06 09:01:34 [notice] 31#31: exit
    2026/04/06 09:01:34 [notice] 1#1: signal 17 (SIGCHLD) received from 34
    2026/04/06 09:01:34 [notice] 1#1: worker process 34 exited with code 0
    2026/04/06 09:01:34 [notice] 1#1: signal 29 (SIGIO) received
    2026/04/06 09:01:34 [notice] 1#1: signal 17 (SIGCHLD) received from 30
    2026/04/06 09:01:34 [notice] 1#1: worker process 30 exited with code 0
    2026/04/06 09:01:34 [notice] 1#1: signal 29 (SIGIO) received
    2026/04/06 09:01:34 [notice] 1#1: signal 17 (SIGCHLD) received from 33
    2026/04/06 09:01:34 [notice] 1#1: worker process 33 exited with code 0
    2026/04/06 09:01:34 [notice] 1#1: signal 29 (SIGIO) received
    2026/04/06 09:01:34 [notice] 1#1: signal 17 (SIGCHLD) received from 29
    2026/04/06 09:01:34 [notice] 1#1: worker process 29 exited with code 0
    2026/04/06 09:01:34 [notice] 1#1: signal 29 (SIGIO) received
    2026/04/06 09:01:34 [notice] 1#1: signal 17 (SIGCHLD) received from 32
    2026/04/06 09:01:34 [notice] 1#1: worker process 32 exited with code 0
    2026/04/06 09:01:34 [notice] 1#1: signal 29 (SIGIO) received
    2026/04/06 09:01:34 [notice] 1#1: signal 17 (SIGCHLD) received from 31
    2026/04/06 09:01:34 [notice] 1#1: worker process 31 exited with code 0
    2026/04/06 09:01:34 [notice] 1#1: exit
    2026/04/06 09:09:29 [notice] 1#1: using the "epoll" event method
    2026/04/06 09:09:29 [notice] 1#1: nginx/1.29.7
    2026/04/06 09:09:29 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
    2026/04/06 09:09:29 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
    2026/04/06 09:09:29 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
    2026/04/06 09:09:29 [notice] 1#1: start worker processes
    2026/04/06 09:09:29 [notice] 1#1: start worker process 29
    2026/04/06 09:09:29 [notice] 1#1: start worker process 30
    2026/04/06 09:09:29 [notice] 1#1: start worker process 31
    2026/04/06 09:09:29 [notice] 1#1: start worker process 32
    2026/04/06 09:09:29 [notice] 1#1: start worker process 33
    2026/04/06 09:09:29 [notice] 1#1: start worker process 34
    ```
    

## 9. Git 설정 및  Github 연동

### 9-1. 사용자 정보 설정

```bash
cla6shade8560@c4r4s4 e1-1 % git config --global user.name "cla7shade"
cla6shade8560@c4r4s4 e1-1 % git config --global user.email "cla7shade@github.com"
```

```bash
git config --global credentials.helper store
```

### 9-2. github 저장소 연결

```bash
cla6shade8560@c4r4s4 e1-1 % git remote -v
origin  https://github.com/cla7shade/codyssey-academy.git (fetch)
origin  https://github.com/cla7shade/codyssey-academy.git (push)
```

```bash
credential.helper=osxkeychain
credentials.helper=store
user.name=cla7shade
user.email=cla7shade@github.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/cla7shade/codyssey-academy.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
```
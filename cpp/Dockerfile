FROM ubuntu:latest
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y cppcheck clang-tidy clang && \
  apt-get install -y curl git htop man unzip vim wget

ENV HOME /root
WORKDIR /root
CMD ["bash"]

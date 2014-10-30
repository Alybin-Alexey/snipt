build-essential:
  pkg.installed:
    - pkgs:
      - build-essential

iptables:
  pkg.installed:
    - pkgs:
      - iptables

system:
  pkg.installed:
    - pkgs:
      - cmake
      - curl
      - exuberant-ctags
      - git
      - htop
      - libpq-dev
      - libxml2-dev
      - libxslt1-dev
      - mercurial
      - python-dev
      - tree

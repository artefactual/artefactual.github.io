===============
Developer Guidelines
===============

Each project has its own Contributing Guidelines, which will give specific
informtation about submitting code to the project. Below you will find specific
guidance on getting started with contributing to AtoM, Archivematica or Enduro.

Useful resources on using Git
-----------------------------

Interactive Git Tutorial: https://learngitbranching.js.org
Git Advanced Cheatsheet: https://dev.to/said7388/git-cheatsheet-that-will-make-you-a-master-in-git-11l4
[SWTM-2088_Atlassian-Git-Cheatsheet.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/158b49d1-4ef0-411d-8143-8c92876358b1/SWTM-2088_Atlassian-Git-Cheatsheet.pdf)
Atlassian’s Git Tutorials: https://www.atlassian.com/git/tutorials

Opening pull requests
----------------------

Artefactual uses [GitHub's pull request feature](https://help.github.com/articles/using-pull-requests)
for code review. Every change being submitted to an Artefactual project should
be submitted as a pull request to the appropriate repository, and the
appropriate branch - in general, to the latest development branch
(named ```qa/[verison]```). A pull request being submitted for code review
should only contain commits covering a related section of code. Try not to
bundle unrelated changes together in one branch; it
makes review harder.


Commit summaries should be short (no more than 50 characters) and clear.

Your commit history should tell a clear story of changes being made.
Consider the following:
* Treat each commit as a minimal coherent idea
* Any refactoring and remaning should be a separate commit to any functional changes
* Every feature or improvement should be a separate commit
* Any moved or changed code should be kept in separate commits from each other
* Squash any commits that fix test errors (such as linting errors)

For more information on creating quality pull requests and managing
commit history, watch [Alya Abbott's Fosdem 2026 presentation](https://fosdem.org/2026/schedule/event/L7ERNP-prs-maintainers-will-love/).


Here are a few blog posts from around the web that offer more help and
overviews using pull requests:

* The GitHub blog has a post on ["how to write the perfect pull request"](https://github.com/blog/1943-how-to-write-the-perfect-pull-request)
* The SpringSource community blog has [useful a post on pull requests](https://spring.io/blog/2010/12/21/social-coding-in-spring-projects)
* Otaku, Cedric's Blog has a [quick guide to pull requests](https://www.beust.com/weblog/a-quick-guide-to-pull-requests/)

Useful commands for gettting started
------------------------------------

Finding files with keywords
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To help you navigate the code bases, doing keyword searches is useful.
You can use a tool called ``ripgrep`` which is a variant of ``grep``.

Usage:

``rg --vimgrep --type-not xml --smart-case <keyword/pattern to search>``

If you use this frequently, you can save this as an alias of you choice by
adding this to your ``~/.zshrc`` or ``~/.bashrc`` files.

```
alias ack="rg --vimgrep --type-not xml --smart-case" 
# Usage: ack <keyword/pattern to search>
```

Setting up some local aliases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to add aliases for commonly used commands to your terminal,
which act as a kind of short-cut to typing out longer commands. This is not
recommended for a production instance, but can be useful in the development
environment for testing, where we are often having to purge and rebuild our
environments.

Aliases can be added to the .bashrc file in your root directory. the dot
before the filename means it is a hidden file - you can see all files in a
directory including hidden ones with: ls -a. Generally, the .bashrc file can
be found in our root directory, so we'll change directories there, and then
find it:

```
cd
ls -a
```

You can open the file with nano, which is a simple text editor inside
your terminal:

``nano .bashrc``

You'll see other default aliases used in bash in there, where you can get
a sense of the syntax. Essentially, the syntax to add an alias is:
``alias XXX='[command]''``. Scroll to the very bottom of the file and add
your aliases there, to keep them separate and easy to find. If you do make
yourself some aliases, it is critical they are unique so they will not
interfere with existing commands! Here is an example of some set up in a
Docker environment for AtoM:

.. code-block:: 
    alias DockerUp='cd ~/Desktop/atom-docker/atom && export COMPOSE_FILE="$PWD/docker/docker-compose.dev.yml" && docker compose up -d'
    alias DS='docker compose exec atom php -d memory_limit=-1 symfony'
    alias DockerDown='cd ~Desktop/atom-docker/atom && docker compose down'
    alias DockerLoad='bash /home/username/Deskop/atom-docker/load-demo-docker.sh'
    alias DC='docker compose exec'
    alias DockerSQL='docker compose exec percona mysql -u atom -p atom;'

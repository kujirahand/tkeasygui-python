# TkEasyGUI Package Developer's Guide

- Please feel free to ask questions in the [issue tracker](https://github.com/kujirahand/tkeasygui-python/issues).
- If you have any requests for new features, please let us know.
  - [Discord > TkEasyGUI](https://discord.gg/NX8WEQd42S)
- Pull requests are highly welcome.
  - When sending a pull request, it would be appreciated if you could include a sample to verify the changes. Please add the file to the tests directory.
  - It would be helpful if you could include the issue number related to the commit. (example) [#96](https://github.com/kujirahand/tkeasygui-python/issues/96).

## Task runner

- Using [Task runner task](https://taskfile.dev/)
  - [Taskfile.yaml](/Taskfile.yml)

```sh
# check all task
task -a
# run viewer
task run
```

## Lint

```sh
task check
task lint
```

## Build documents

```sh
task build-docs
```

## Deploy to pypi

```sh
task deploy-test
task deploy-main
```

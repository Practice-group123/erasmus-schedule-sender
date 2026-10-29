# Contributing

[English](#english) | [Русский](#русский)

---

## English


## Workflow

1. Pick a task from the **Ready** column on the project board.
2. Assign yourself to the issue and move it to **In progress**.
3. Create a branch from an up-to-date `main`.
4. Commit your work, push the branch, open a pull request.
5. Move the card to **In review**. Review is requested automatically.
6. Fix review comments, resolve all conversations.
7. After approval the PR is merged with **Squash and merge**. The issue closes and the card moves to **Done**.

Direct pushes to `main` are blocked. Every change goes through a PR.

## Branches

Format: `type/short-description` (lowercase, words separated by `-`).

| Type       | Use for                          | Example                       |
|------------|----------------------------------|-------------------------------|
| `feature/` | new functionality                | `feature/drive-parser`        |
| `fix/`     | bug fixes                        | `fix/empty-schedule-crash`    |
| `refactor/`| code changes without new behavior| `refactor/split-sender-module`|
| `docs/`    | documentation only               | `docs/setup-instructions`     |
| `chore/`   | config, dependencies, CI         | `chore/add-linter`            |

```bash
git checkout main
git pull
git checkout -b feature/drive-parser
```

## Commit messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
type: short description in imperative mood
```

- `feat: add Google Drive schedule parser`
- `fix: handle empty schedule file`
- `refactor: move config loading to separate module`
- `docs: add setup steps to README`
- `chore: add requirements.txt`
- `test: add tests for date parsing`

Rules:
- English, lowercase after the colon, no period at the end.
- Imperative mood: "add", not "added" / "adds".
- One commit = one logical change. Avoid `fix`, `wip`, `asdf`.
- Up to ~72 characters in the first line.

Since PRs are squash-merged, **the PR title becomes the commit in `main`**, so write the PR title in the same format.

## Pull requests

- Title in commit format: `feat: add Google Drive schedule parser`
- Fill in the PR template.
- Link the issue: `Closes #12` in the description.
- Keep PRs small. Big PR = slow review.
- Before opening a PR, update your branch with `main`:
  ```bash
  git checkout main
  git pull
  git checkout feature/drive-parser
  git merge main
  ```
- Make sure the code runs locally.

## Code style

- Follow PEP 8.
- `snake_case` for files, functions and variables; `PascalCase` for classes.
- Add new dependencies to `requirements.txt` in the same PR.

## Secrets

Never commit `.env` anyway you cant do it, API keys, tokens or `credentials.json`. The repository is **public**
If you committed a secret by accident, tell the team lead immediately: the key must be revoked, deleting the commit is not enough.


---

## Русский

# Участие в разработке

## Процесс работы

1. Возьмите задачу из колонки **Ready** на доске проекта.
2. Назначьте себя на issue и перенесите карточку в **In progress**.
3. Создайте ветку от актуального `main`.
4. Закоммитьте изменения, запушьте ветку, откройте pull request.
5. Перенесите карточку в **In review**. Ревью запросится автоматически.
6. Исправьте замечания ревью, закройте все обсуждения.
7. После одобрения PR мержится через **Squash and merge**. Issue закрывается, карточка уезжает в **Done**.

Пушить напрямую в `main` нельзя. Любые изменения только через PR.

## Ветки

Формат: `type/short-description` (маленькими буквами, слова через `-`).

| Тип         | Для чего                          | Пример                        |
|-------------|-----------------------------------|-------------------------------|
| `feature/`  | новый функционал                  | `feature/drive-parser`        |
| `fix/`      | исправление багов                 | `fix/empty-schedule-crash`    |
| `refactor/` | изменения кода без нового поведения | `refactor/split-sender-module`|
| `docs/`     | только документация               | `docs/setup-instructions`     |
| `chore/`    | конфиги, зависимости, CI          | `chore/add-linter`            |

```bash
git checkout main
git pull
git checkout -b feature/drive-parser
```

## Сообщения коммитов

Используем [Conventional Commits](https://www.conventionalcommits.org/ru/):

type: short description in imperative mood


- `feat: add Google Drive schedule parser`
- `fix: handle empty schedule file`
- `refactor: move config loading to separate module`
- `docs: add setup steps to README`
- `chore: add requirements.txt`
- `test: add tests for date parsing`

Правила:
- На английском, после двоеточия с маленькой буквы, без точки в конце.
- Повелительное наклонение: «add», а не «added» / «adds».
- Один коммит = одно логическое изменение. Никаких `fix`, `wip`, `asdf`.
- Первая строка до ~72 символов.

Так как PR мержатся через squash, **название PR становится коммитом в `main`**, поэтому пишите название PR в том же формате.

## Pull requests

- Название в формате коммита: `feat: add Google Drive schedule parser`
- Заполните шаблон PR.
- Привяжите задачу: `Closes #12` в описании.
- Делайте PR небольшими. Большой PR = долгое ревью.
- Перед открытием PR подтяните изменения из `main` в свою ветку:
  ```bash
  git checkout main
  git pull
  git checkout feature/drive-parser
  git merge main
  ```
- Убедитесь, что код запускается локально.

## Стиль кода

- Следуйте PEP 8.
- `snake_case` для файлов, функций и переменных; `PascalCase` для классов.
- Новые зависимости добавляйте в `requirements.txt` в том же PR.

## Секреты

Никогда не коммитьте `.env` а вы и не сможете, API-ключи, токены и `credentials.json`. Репозиторий **публичный**.
Если случайно закоммитили секрет, сразу сообщите тимлиду: ключ нужно отозвать, удалить коммит недостаточно.

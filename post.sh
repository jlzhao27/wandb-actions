curl \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/jlzhao27/wandb-actions/actions/workflows/main.yml/dispatches \
  -d '{"ref":"main","inputs":{"job-config":"{\"epochs\": 100}"}}'

echo $?

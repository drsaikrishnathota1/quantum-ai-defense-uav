# RunPod Setup Notes

## Build Docker image locally

```bash
docker build -t quantum-ai-defense-uav .
```

## Run locally

```bash
docker run --rm quantum-ai-defense-uav
```

## Run on RunPod

- Use `python:3.11-slim` or a similar base in a custom image, or upload this Dockerfile as your template.
- Mount or clone this repository into `/app`.
- Run:

```bash
cd /app
pip install -r requirements.txt
bash scripts/run_experiment.sh
```

## Future steps

- When quantum or AI libraries are added, update `requirements.txt`.
- Optionally add a `scripts/run_batch_experiments.sh` and use that as the default CMD.

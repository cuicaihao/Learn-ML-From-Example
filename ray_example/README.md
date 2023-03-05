# Learning Note: Ray

Ray AI Runtime (AIR) is a scalable and unified toolkit for ML applications. AIR enables simple scaling of individual workloads, end-to-end workflows, and popular ecosystem frameworks, all in just Python.

![Ray AIR](https://docs.ray.io/en/latest/_images/ray-air.svg)


AIR builds on Ray’s best-in-class libraries for Preprocessing, Training, Tuning, Scoring, Serving, and Reinforcement Learning to bring together an ecosystem of integrations.

## ML Compute, Simplified
Ray AIR aims to simplify the ecosystem of machine learning frameworks, platforms, and tools. It does this by leveraging Ray to provide a seamless, unified, and open experience for scalable ML:

![Why ARI](https://docs.ray.io/en/latest/_images/why-air-2.svg)
1. Seamless Dev to Prod: AIR reduces friction going from development to production. With Ray and AIR, the same Python code scales seamlessly from a laptop to a large cluster.

2. Unified ML API: AIR’s unified ML API enables swapping between popular frameworks, such as XGBoost, PyTorch, and HuggingFace, with just a single class change in your code.

3. Open and Extensible: AIR and Ray are fully open-source and can run on any cluster, cloud, or Kubernetes. Build custom components and integrations on top of scalable developer APIs.

## When to use AIR?
AIR is for both data scientists and ML engineers alike.

![When AIR](https://docs.ray.io/en/latest/_images/when-air.svg)

For data scientists, AIR can be used to scale individual workloads, and also end-to-end ML applications. For ML Engineers, AIR provides scalable platform abstractions that can be used to easily onboard and integrate tooling from the broader ML ecosystem.

## Quick Start
Below, we walk through how AIR’s unified ML API enables scaling of end-to-end ML workflows, focusing on a few of the popular frameworks AIR integrates with (XGBoost, Pytorch, and Tensorflow). The ML workflow we’re going to build is summarized by the following diagram:

![Why AIR](https://docs.ray.io/en/latest/_images/why-air.svg)
AIR provides a unified API for the ML ecosystem. This diagram shows how AIR enables an ecosystem of libraries to be run at scale in just a few lines of code.
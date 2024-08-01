# Brief Notes on Large Language Models

## Introduction
- **Large Language Model (LLM) Components**:
  - Parameters file: Contains weights/parameters of the neural network.
  - Run file: Contains code to operate the neural network.
- **Self-Contained System**: Can run on a System without internet connectivity.
- **Model Training**: Involves compressing large amounts of internet data (a lot of data) into a format for training.

## Text Compression and Inference
- **Text Compression**: LLMs use lossy compression to process large amounts of text data.
- **Next Word Prediction**: Main purpose is to predict the next word in a sequence.
- **Inference**: Simple process of generating what comes next by sampling from the model.
- **Generated Text**: May not be perfectly accurate; contains some randomness.

## Training Stages
- **Pre-training**:
  - Trained on large datasets to learn grammar, facts, and reasoning.
  - Generally uses data acquired from internet.
  - Requires specialized supercomputers or arrays of GPUs.
- **Fine-tuning**:
  - Trained on specific tasks or domains.
  - Computationally cheaper; allows faster iterations.
  - Can involve human-machine collaboration.
- **Assistant Models**: Fine-tuned models for specific tasks like answering questions.

## Performance and Scaling
- **Performance**: Depends on the number of parameters and training data.
- **Scaling**: Bigger models trained on more data yield better results.
- **Computing Gold Rush**: Larger GPU clusters and more data sought for better LLM performance.

## Capabilities and Future Directions
- **Multimodality**: LLMs can process and utilize information from images and audio.
- **System One and System Two Thinking**: Distinction between fast and slow thinking processes.
- **Self-Improvement**: Potential for LLMs to surpass human expertise through self-training.

## Security Challenges
- **Jailbreak Attacks**: Tricking LLMs into answering harmful queries.
- **Prompt Injection Attacks**: Exploiting LLM's ability to attend to specific prompts.
- **Shield-Breaking Attacks**: Bypassing security measures.
- **Data Poisoning/Backdoor Attacks**: Training LLMs on harmful data.
- **Defenses**: Developed over time and incorporated into models.

## Examples of Attacks
- **Bing Search Engine**: Prompt injection attack leading to fraudulent links.
- **Google Docs**: Prompt injection attack attempting to exfiltrate private information.

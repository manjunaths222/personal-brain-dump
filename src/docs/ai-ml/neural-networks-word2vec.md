---
title: "Neural Networks Word2Vec"
---

Neural Networks / Word2Vec

PART 1 — Neural Networks Core Foundation

What a Neural Network Is: A function that learns parameters (weights) from data to make predictions.
Input → Weighted Sum → Activation → Output
z = W·x + b, a = activation(z)

Two Phases:
1. Training: inputs + correct answers → forward pass → loss → backpropagation → weights change
2. Prediction/Inference: inputs → apply learned weights → output (weights do NOT change)

Why Activation Functions:
Without activation, multiple layers collapse into one linear equation.
- Sigmoid → probabilities
- ReLU → feature extraction  
- Softmax → class selection

Key Truth: Weights store knowledge. Activations interpret signals.

PART 2 — CBOW (Continuous Bag of Words)

What CBOW Is: Context words → Target word (self-supervised learning)
Architecture: Context (one-hot) → Embedding Layer (Hidden) → Output Layer (Softmax)

Training Steps:
1. One-hot encode each context word
2. Embedding Lookup: one-hot × W = embedding (W = embedding matrix, vocab × embedding_dim)
3. Context Combination: h = average(embeddings of context words)
4. Output Prediction: h × W' → scores → softmax
5. Backprop: updates both W and W'

After Training: Output layer discarded, W matrix kept as word vectors.

CBOW Key Insights:
- Hidden layer = embedding lookup (no activation in hidden layer)
- Output layer is teaching scaffold, not final product
- Both W (input) and W' (output) are learned; W is typically kept

PART 3 — Skip-Gram

What Skip-Gram Is: Target word → Context words (opposite of CBOW)
Training pairs: (deep→love), (deep→learning), (love→I), (love→deep)
One target → many training pairs

Negative Sampling Optimization:
- 1 positive word + k negative random words
- Binary classification instead of full softmax: scalable!
- (deep, love) → 1, (deep, car) → 0

CBOW vs Skip-Gram Comparison:
- Direction: Context→Target vs Target→Context
- Speed: Faster vs Slower
- Rare words: Weaker vs Stronger
- Context handling: Averaged vs Individual

Both models learn W (input embeddings) and W' (output embeddings).
Practice: Keep W, discard W'. W answers "What does this word mean?", W' answers "What words tend to appear around this word?"

Ultimate Mental Model:
- CBOW = "guess the missing word"
- Skip-Gram = "describe the neighborhood"
- Training = learning meaning
- Embeddings = coordinates in meaning space

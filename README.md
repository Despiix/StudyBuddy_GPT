# StudyBuddy_GPT

A GPT chatbot to help you study and create flashcards. The program is still under development
but if you have any suggestions don't hesitate to let me know.

- batch_size: This parameter determines the number of independent sequences that will be processed in parallel during training. 
A larger batch size can speed up training, but it requires more memory.

- block_size: This parameter sets the maximum context length for predictions. 
The GPT model generates predictions based on the context it receives as input, and this parameter sets the maximum length of that context.

- max_iters: This parameter sets the maximum number of training iterations for the GPT model.

- eval_interval: This parameter sets the number of training iterations, after which the model’s performance will be evaluated.

- learning_rate: This parameter determines the learning rate for the optimizer during training.

- device: This parameter sets the device (CPU or GPU) on which the GPT model will be trained.

- eval_iters: This parameter sets the number of training iterations, after which the model’s performance will be evaluated and saved.

- n_embd: This parameter sets the number of embedding dimensions for the GPT model.
  The embedding layer maps the input sequence into a high-dimensional space, and this parameter determines the size of that space.

- n_head: This parameter sets the number of attention heads in the multi-head attention layer of the GPT model. 
  The attention mechanism allows the model to focus on specific parts of the input sequence.

- n_layer: This parameter sets the number of layers in the GPT model.

- dropout: This parameter sets the dropout probability for the GPT model. 
  Dropout is a regularization technique that randomly drops out some of the neural network’s nodes during training to prevent overfitting.

Read dataset link: https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
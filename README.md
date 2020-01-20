# cliplot

Plot data from `stdin` on the command line.

## Installation

```
git clone https://github.com/aaronsnoswell/cliplot.git
cd cliplot
pip install -r requirements.txt
```

## Usage

`demo.txt` contains text output from running a simulation (in this case,
training a Maximum Entropy IRL model).
The output looks as follows...

```
Iteration 1
 > θ = [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 > Computing alpha, beta with minmax
 > Computing efv
 > Time ab = 146.02761818491854 efv = 1455.7945449089166
 > E_θ[ϕ] = [2.07608850e+01 1.99151245e+03 5.50348372e+01 3.03889296e+04
 8.18417358e-09 4.85654302e-01 6.55617223e-02 3.24553828e+04
 3.03761575e-01 3.92033273e-08 3.24562376e+04 2.33698997e-04
 3.24562378e+04 1.45103691e-17]
 > ∇ = [ 2.00163023e+03 -1.75345920e+03  1.94354770e+02 -2.91506472e+04
  4.08349632e+02  2.92222619e+02  1.04190189e+02 -2.95204085e+04
  6.52471711e+00  7.47913825e+02 -2.99272642e+04  4.72229014e+02
 -2.87420797e+04  3.59583121e+01]
 > |∇| = 58746.30770160538
 > NLL = 453.0705616217263
 > Saved checkpoint to results/mdl.me.ae-4.4.pkl
Iteration 2

[snip]
```

Say you are ssh-ed into a server where this simulation is running, and want to
check on it's progress without actually downloading the model checkpoint etc.
If the progress metric we care about is the gradient magnitude, which is
printed on the lines ` > |∇| = 58746.30770160538`, we could plot the model's
training progress as follows;

```
cat demo.txt | grep \|∇\|\ =\ | sed s/\>\ \|∇\|\ =\ // | ~/cliplot/cliplot.py
```

Which would produce the following terminal output;

```
  160000 +------+**-----+------+------+-------+------+------+-------+------+
         |   **  ***                         *                             |
  140000 +   **  ***                         *                             +
         |   *** ***                         *                             |
         |   *** ***                         *                             |
  120000 +   *** ***                         *                             +
         |   *** ***                         *                             |
  100000 +   *** ***                         *                             +
         |   *** ***                 *       *                             |
   80000 +   *** ***                 *       *                             +
         |   *** *** *               *       **                            |
         |****** *** *  ***        ***** * * **  *                         |
   60000 ** **** *** *  ***        ***** * * **  *                         +
         |  **** *** *  ***        ***** * * **  *                         |
   40000 +  **** *****  ***   **   ***** * * **  **                        +
         |  **** ****** ***   **   ***** *** **  **                        |
         |  **** ****** ****  **   ********* **  **                        |
   20000 +  **** ** *** **** ** *  ********* **  **                        +
         |  **** ** ******** ** *  ************* ***                       |
       0 +---******-***********+***************************************----+
         0      20      40     60     80     100    120    140     160    180
```

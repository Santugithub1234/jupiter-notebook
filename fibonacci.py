{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d3003fc8",
   "metadata": {},
   "source": [
    "# Fibonacci series upto 34 \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "43107fc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:34\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"enter a number:\"))\n",
    "x = 0\n",
    "y = 1\n",
    "z = 0\n",
    "while (z<=n):\n",
    "    print(z)\n",
    "    x = y\n",
    "    y = z\n",
    "    z = x + y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ca49050",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lazarevtill/deep/blob/master/nti_var.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "NHRktYVGlEqB",
        "colab_type": "code",
        "outputId": "d616bf85-9b09-46bc-9f06-b2b554de231b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 127
        }
      },
      "cell_type": "code",
      "source": [
        "def save(name='test', fmt='png'):\n",
        "    plt.savefig('{}.{}'.format(name, fmt), fmt=fmt)\n",
        "\n",
        "\n",
        "def set_ticks(mv):\n",
        "    plt.figure()\n",
        "    plt.plot(np.asarray(range(len(mv))), mv)\n",
        "    plt.grid()\n",
        "    plt.xlabel('n, номер отсчёта')\n",
        "    plt.ylabel('v, электрический потенциал')\n",
        "    plt.title('ЭКГ')\n",
        "\n",
        "\n",
        "def main():\n",
        "    set_ticks(g)\n",
        "    plt.show()\n",
        "    # save()\n",
        "\n",
        "f = []\n",
        "s = []\n",
        "x = input().split(' ')\n",
        "for i in range(len(x)):\n",
        "    nnnn, b = map(int, x[i].split(','))\n",
        "    f.append(a)\n",
        "    s.append(nnnn)\n",
        "# print(f, s)\n",
        "x=f\n",
        "for m in range(2):\n",
        "    \n",
        "    N = 40\n",
        "    # Первый алгоритм (Выделение QRS)\n",
        "    g1 = []\n",
        "    for n in range(len(x)):\n",
        "    a = []\n",
        "    for i in range(1, N + 1):\n",
        "        if n - i >= 0:\n",
        "            an = ((x[n - i + 1] - x[n - i]) ** 2) * (N - i + 1)\n",
        "            a.append(an)\n",
        "    g1.append(sum(a))\n",
        "    # Второй алгоритм (фильтрация, нз зачем)\n",
        "    # g = []\n",
        "    # for n in range(len(x)):\n",
        "    #     a = []\n",
        "    #     for i in range(1, N):\n",
        "    #         if n - i >= 0:\n",
        "    #             an = g1[n - i]\n",
        "    #             a.append(an)\n",
        "    #     g.append(sum(a)/N)\n",
        "    # Поиск пиков среди g\n",
        "    g = g1[:]\n",
        "    p = []\n",
        "    th = 0.5 * max(g)\n",
        "    for n in range(len(g)):\n",
        "    if g[n] <= th:\n",
        "        continue\n",
        "    flag = False\n",
        "    for i in range(1, N + 1):\n",
        "        if n - i >= 0:\n",
        "            if g[n] <= g[n - i]:\n",
        "                flag = True\n",
        "                break\n",
        "        if n + i < len(g):\n",
        "            if g[n] < g[n + i]:\n",
        "                flag = True\n",
        "                break\n",
        "    if flag:\n",
        "        continue\n",
        "    p.append(n)\n",
        "\n",
        "    i = 0\n",
        "    while i != len(p):\n",
        "    if abs(p[i] - p[i - 1]) * 2 <= 400:\n",
        "        del p[i]\n",
        "    else:\n",
        "        i += 1\n",
        "\n",
        "# ЗАДАЧА 1\n",
        "print(len(p))\n",
        "\n",
        "    # ЗАДАЧА 2 (фэйлится на 2-ом тесте)\n",
        "    # intervals = []\n",
        "    # for i in range(len(p)):\n",
        "    #     if i != 0:\n",
        "    #         intervals.append((p[i] - p[i - 1]) * 2)\n",
        "    # print(*intervals)\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    import numpy as np\n",
        "    import matplotlib.pyplot as plt\n",
        "    main()\n",
        "\n"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-2-3b0fe7b49719>\"\u001b[0;36m, line \u001b[0;32m34\u001b[0m\n\u001b[0;31m    a = []\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
          ]
        }
      ]
    }
  ]
}
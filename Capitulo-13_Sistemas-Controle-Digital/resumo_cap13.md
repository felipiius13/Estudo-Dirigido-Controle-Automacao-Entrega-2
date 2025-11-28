# Resumo Teórico: Capítulo 13 - Sistemas de Controle Digital

O Capítulo 13 introduz o controle realizado por computadores (discreto), que é como a grande maioria dos sistemas modernos opera.

**Conceitos Principais:**
* **Amostragem (Sampling):** A conversão de sinais contínuos (analógicos) para discretos (digitais). O Teorema de Nyquist-Shannon diz que devemos amostrar pelo menos duas vezes mais rápido que a maior frequência do sistema para não perder informações (evitar *aliasing*).
* **Transformada Z:** É a ferramenta matemática para sistemas digitais, análoga à Transformada de Laplace. Mapeamos o plano 's' para o plano 'z'.
    * A estabilidade no plano Z exige que os polos estejam **dentro do círculo unitário** ($|z| < 1$).
* **Segurador de Ordem Zero (ZOH):** É o componente (DAC) que mantém o valor digital constante até a próxima amostra, criando aquele formato de "escada" no sinal de controle real.

### Conexão com a Indústria 4.0

* **IIoT, Latência e Edge Computing:** Na Indústria 4.0, sensores enviam dados via rede sem fio (IIoT). O "Tempo de Amostragem" ($T_s$) deixa de ser apenas uma escolha matemática e passa a depender da velocidade da rede e da latência. Se a rede Wi-Fi/5G oscila, a amostragem pode atrasar (Jitter). O Controle Digital moderno precisa lidar com perda de pacotes de dados. Para resolver isso, usa-se **Edge Computing**: o algoritmo de controle (PID digital) roda em um hardware na borda (no próprio motor), garantindo amostragem rápida e estável, enviando para a nuvem apenas os relatórios de desempenho, não o sinal de controle crítico.

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

//#define bool int
#define true 1
#define false 0

#define MAX_VERTICES 4096
#define LOG_MAX_VERTICES 12
#define TAM_NACO 32 				// tipo do NACO: unsigned int; tamanho do NACO: sizeof(unsigned int) = 4
#define LOG_TAM_NACO 5

#define MAX_V_NACOS (MAX_VERTICES >> LOG_TAM_NACO)
#define LOG_MAX_V_NACOS (LOG_MAX_VERTICES - LOG_TAM_NACO)
#define MAX_ADJ_NACOS (MAX_VERTICES << LOG_MAX_V_NACOS)

#define N_NACOS(n) (((n >> LOG_TAM_NACO) << LOG_TAM_NACO) == n ? (n >> LOG_TAM_NACO) : ((n >> LOG_TAM_NACO)+1))
#define IDX_VIZ(v) (v << LOG_MAX_V_NACOS)
#define IDX_NACO(v) (v >> LOG_TAM_NACO)
#define IDX_EM_NACO(v) (v - (IDX_NACO(v) << LOG_TAM_NACO))

#define NACO(a,u,v) ((a+IDX_VIZ(u))[IDX_NACO(v)])

typedef struct No {
    int valor;
    struct No* prox;
} No;

No* partida(unsigned int R[MAX_ADJ_NACOS]) {
    No* r = (No*)malloc(sizeof(No));
    if (r == NULL) {
        printf("Erro ao alocar memória.\n");
        exit(1);
    }
    r->valor = 0;
    r->prox = NULL;
    return r;
}

int alvo(No* r) {
    return r->valor;
}


bool chegada(No* r) {
    return (r->prox == NULL);
}

No* avancar(No* r) {
    if (r->prox == NULL) {
        return r;
    }
    return r->prox;
}
bool subconj(unsigned int R[MAX_ADJ_NACOS], No* vizinhos) {
    No* atual = vizinhos;
    while (atual != NULL) {
        if (!(NACO(R, atual->valor, atual->valor) & (1 << IDX_EM_NACO(atual->valor)))) {
            return false;
        }
        atual = atual->prox;
    }
    return true;
}

No* vizinhos(unsigned int adjMatrix[MAX_ADJ_NACOS], int valor) {
    No* listaVizinhos = NULL;

    for (int i = 0; i < MAX_VERTICES; i++) {
        if (NACO(adjMatrix, valor, i) & (1 << IDX_EM_NACO(i))) {
            No* novoVizinho = (No*)malloc(sizeof(No));
            if (novoVizinho == NULL) {
                printf("Erro de alocação");
                exit(1);
            }
            novoVizinho->valor = i;
            novoVizinho->prox = listaVizinhos;
            listaVizinhos = novoVizinho;
        }
    }

    return listaVizinhos;
}


void retirar(No* r) {
    if (r == NULL) {
        printf("Lista removida");
        return;
    }
    No* atual = r;
    r = atual->prox;
    free(atual);
}

// Função para verificar se um subconjunto define uma clique no grafo
bool verificaClique(int numVertices, unsigned int adjMatrix[MAX_ADJ_NACOS], unsigned int subset[MAX_V_NACOS]) {
    unsigned int R[MAX_ADJ_NACOS];
    memcpy(R, adjMatrix, N_NACOS(numVertices));
    No * r = partida(R);
    while (!chegada(r)) {
    	retirar(r);
    	if (!subconj(R, vizinhos(adjMatrix, alvo(r))))
    		return false;
    	r = avancar(r);
    }
    return true;
}

// Função para medir o tempo de execução médio da função verificaClique
double medirTempoExecucao(int numVertices, unsigned int adjMatrix[MAX_ADJ_NACOS], unsigned int subset[MAX_V_NACOS], int repeticoes) {
    clock_t inicio, fim;
    inicio = clock();
    for (int i = 0; i < repeticoes; i++)
        verificaClique(numVertices, adjMatrix, subset);
    fim = clock();
    double tempoTotal = (double)(fim - inicio) / CLOCKS_PER_SEC;

    return tempoTotal / repeticoes;
}

// Função para gerar um grafo aleatório com base nos parâmetros especificados
void gerarGrafoAleatorio(int numVertices, double densidade, unsigned int adjMatrix[MAX_ADJ_NACOS]) {
    // Limpa a matriz de adjacências
	int numNacos = N_NACOS(numVertices);
	for (int i = 0; i < numVertices; i++) {
		int idx_i = IDX_VIZ(i);
		for (int j = 0; j < numNacos; j++) {
			(adjMatrix+idx_i)[j] = 0;
		}
	}

    // Calcula o número esperado de arestas
    int numArestas = (int)(densidade * numVertices * (numVertices - 1) / 2);

    // Define a semente para geração de números aleatórios
    srand(time(NULL));

    // Gera arestas aleatórias até atingir o número esperado
    int count = 0;
    while (count < numArestas) {
        int v1 = rand() % numVertices; // Vértice inicial aleatório
        int v2 = rand() % numVertices; // Vértice final aleatório

        if (v1 != v2 && !(NACO(adjMatrix,v1,v2) & (1 << IDX_EM_NACO(v2)))) {
            // Adiciona a aresta ao grafo
            NACO(adjMatrix,v1,v2) |= (1 << IDX_EM_NACO(v2));
            NACO(adjMatrix,v2,v1) |= (1 << IDX_EM_NACO(v1));
            count++;
        }
    }
}

// Função para estimar o tempo de execução da função verificaClique para diferentes tamanhos de grafos
double* estimarTempoExecucao(int from, int to, int by, int nsamples, double dens, int nrep, double r) {
    int numVertices, subsetSize;
    double *tempos = malloc(((to - from) / by + 1) * sizeof(double));

    printf("Estimar tempo médio de execução\nfrom: %d\nto: %d\nby: %d\nnsamples: %d\ndens: %f\nnrep: %d\nr: %f\n",
    		from, to, by, nsamples, dens, nrep, r);
    fflush(NULL);

    int currentIndex = 0;
    for (int n = from; n <= to; n += by) {
        numVertices = n;
        subsetSize = n * r;

        unsigned int adjMatrix[MAX_ADJ_NACOS];
        unsigned int subset[MAX_V_NACOS];
    	int numNacosSubset = N_NACOS(subsetSize);

        double tempoTotal = 0.0;

        for (int i = 0; i < nsamples; i++) {
            gerarGrafoAleatorio(numVertices, dens, adjMatrix);

            for (int j = 0; j < numNacosSubset; j++) {
            	subset[j] = 0;
            }
            for (int j = 0; j < subsetSize; j++) {
                int vertex = rand() % numVertices; // Escolhe um vértice aleatório
                subset[IDX_NACO(vertex)] |= (1 << IDX_EM_NACO(vertex)); // Adiciona o vértice ao subconjunto
            }

            tempoTotal += medirTempoExecucao(numVertices, adjMatrix, subset, nrep);
        }

        tempos[currentIndex] = tempoTotal / nsamples;
        currentIndex++;
    }

    return tempos;
}

int main() {
    int from = 1024; // Quantidade inicial de vértices
    int to = 4096; // Quantidade final de vértices
    int by = 256; // Incremento na quantidade de vértices
    int nsamples = 10; // Quantidade de grafos por tamanho
    double dens = 0.99; // Densidade esperada dos grafos
    int nrep = 10000; // Quantidade de execuções para medição de tempo de execução
    double r = 0.1; // Fração que determina tamanho do subconjunto

    printf("Parâmetros do experimento:\nMAX_VERTICES: %d\nLOG_MAX_VERTICES: %d\nTAM_NACO: %d\nLOG_TAM_NACO: %d\nMAX_V_NACOS: %d\nLOG_MAX_V_NACOS: %d\nMAX_ADJ_NACOS: %d\n\n",
    		MAX_VERTICES,
			LOG_MAX_VERTICES,
			TAM_NACO,
			LOG_TAM_NACO,
			MAX_V_NACOS,
			LOG_MAX_V_NACOS,
			MAX_ADJ_NACOS);

    double tempos = medirTempoExecucao(from, to, by, nsamples);

    printf("Tempo médio de execução:\n");
    int currentIndex = 0;
    for (int n = from; n <= to; n += by) {
        printf("Número de vértices: %d, Tempo: %e segundos\n", n, tempos);
        currentIndex++;
    }

    //free(tempos);

    return 0;
}

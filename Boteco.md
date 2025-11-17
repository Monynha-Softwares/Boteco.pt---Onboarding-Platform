# 🍺 **Boteco Pro – Plataforma de Gestão Integrada para Bares e Restaurantes**

### *Documento Oficial de Proposta Técnica e de Produto (Monynha Softwares)*

### *Versão 1.0 – MVP de Classe Série A*

---

# **1. Visão Geral da Plataforma**

O **Boteco Pro** é uma plataforma completa de **gestão inteligente para bares, restaurantes, pubs, cafés e pequenos negócios do setor alimentício**, criada pela **Monynha Softwares** — empresa que combina tecnologia moderna, propósito social e excelência em design.

A plataforma foi projetada para resolver problemas reais do setor:
✓ gestão operacional lenta
✓ perda de pedidos
✓ falta de controle de estoque
✓ dificuldades de comunicação interna
✓ ausência de dados consolidados
✓ sistemas caros e antiquados

O Boteco Pro nasce como uma solução **offline-first**, **multiusuário**, **multitenant**, com **colaboração em tempo real**, pensada para funcionar em:

* Desktop (Flet / Flutter Desktop)
* App Mobile (Flutter)
* Web Dashboard (Flutter Web)
* Integração com hardware local (impressoras, PDV, etc.)

Sua base é construída em uma arquitetura moderna com:

* **Flutter** (app + dashboard)
* **Supabase (Postgres + Realtime + Storage + Edge Functions)**
* **Clerk** (autenticação e identidade)
* **Microserviços independentes (Python/Node)**
* **SQLite + sincronização incremental (modo offline local)**
* **Arquitetura multitenant: 1 schema por organização**

---

# **2. Proposta de Valor**

A plataforma oferece:

* **Velocidade operacional** no salão, cozinha e caixa
* **Confiabilidade offline**, mesmo sem internet
* **Gestão centralizada** de produtos, estoque, compras, finanças e relatórios
* **Colaboração em tempo real** entre garçonete, bar, cozinha e caixa
* **Baixo custo**, modelo acessível e escalonável
* **Tecnologia contemporânea**, UX de alto nível (shadcn/ui + Flutter)
* **Inclusão, democratização tecnológica e representatividade**, seguindo os valores Monynha

---

# **3. Perfis de Produto**

O Boteco Pro é distribuído em dois grandes segmentos:

### **3.1 Boteco Pro (Cloud-only)**

Para pequenos comércios que desejam gestão 100% em nuvem.

### **3.2 Boteco Pro Patrão (Local Server + Sync Cloud)**

Para comércios maiores que precisam de:

* Servidor local sempre disponível
* Operação sem internet
* Sincronização periódica com banco global
* Impressoras e PDV diretamente no servidor

---

# **4. Arquitetura Macro da Plataforma**

Resumo técnico baseado no documento **“Proposta Técnica Boteco Pro – Flutter + Clerk + Supabase”**.

### **4.1 Stack Tecnológica**

* Frontend: **Flutter** (mobile, web, desktop)
* Backend: **Supabase** + Edge Functions
* Autenticação & Identidade: **Clerk**
* Banco Global: **Supabase Postgres**
* Modo Offline: **SQLite (Drift)**
* Sincronização: **delta-sync via change-log**
* Eventos em Tempo Real: **Supabase Realtime**
* Hospedagem: **Coolify / Docker / Kubernetes**

### **4.2 Multi-Organização / Multitenancy**

* **Schema global:** `public` → cadastro de usuários, botecos, planos, billing
* **Schema privado:** `org_boteco_slug` → dados operacionais exclusivos
* **Isolamento via RLS**
* **search_path dinâmico** por organização
* **trigger universal de change-log**

---

# **5. Sistema de Microsserviços**

O ecossistema Boteco Pro é dividido em serviços independentes:

### **5.1 Auth Service (Clerk Integration)**

* criação de contas
* verificação de identidade
* roles (owner, manager, staff)
* troca de organização

### **5.2 Barnostri – Painel Administrativo (Onboarding Service)**

Responsável pelo fluxo principal de entrada:

1. criação da conta
2. cadastro do comércio
3. escolha do plano
4. checkout/pagamento
5. provisionamento do schema privado
6. envio dos acessos

### **5.3 Billing & Subscription Service**

* integração com Stripe/Asaas
* webhooks de pagamento
* status da assinatura
* revalidação periódica
* bloqueio / suspensão automática

### **5.4 Provisioning Service (Schema Factory)**

* cria schema `org_{slug}`
* popula tabelas iniciais
* aplica migrations
* registra logs de criação

### **5.5 Notifications Service**

* emails
* push notifications
* alertas de estoque
* alertas de vendas
* confirmação de pagamento

### **5.6 Business Core Services**

Separados por domínio:

* **Orders Service** (comandas, mesas, pedidos)
* **Catalog Service** (produtos, cardápio, receitas)
* **Inventory Service** (insumos, estoque, movimentos)
* **Purchases Service** (fornecedores, compras)
* **Staff Service** (funcionários, jornadas, roles)
* **Reports Service** (dashboard, análises, métricas D-1)
* **Kitchen Display System (KDS)**
* **POS/Payments Service**

---

# **6. Funcionalidades do MVP**

O MVP Série A precisa entregar **valor real imediato**. Abaixo estão as features essenciais.

---

## **6.1 Onboarding e Assinatura**

* Criar conta via Clerk
* Cadastro do comércio
* Upload de documentos fiscais
* Escolha de plano e método de pagamento
* Criação automática do schema Supabase
* Envio automático de e-mail com credenciais
* Painel inicial de boas-vindas

---

## **6.2 Painel Administrativo (Web)**

* Visão geral do negócio
* Configuração da organização
* Cadastro de equipe
* Definição de roles e permissões
* Configuração de cardápio
* Configuração de mesas
* Ativação de integrações (impressora, PDV, etc.)

---

## **6.3 App Operacional (Mobile/Tablet)**

### **Salão**

* abrir mesa
* adicionar pedido
* separar por categorias (bebidas, comidas, combos)
* observações do cliente
* fechamento parcial/total

### **Cozinha (KDS)**

* exibir pedidos em tempo real
* controlar status (preparando, pronto, entregue)

### **Caixa**

* registrar pagamentos
* dividir conta
* recibos
* integração futura com pagamentos digitais

---

## **6.4 Estoque**

* cadastro de insumos
* movimentações (entrada/saída)
* alertas (baixa quantidade)
* integração com receitas/produtos

---

## **6.5 Relatórios**

* vendas do dia
* vendas por categoria
* produtos mais vendidos
* desperdício / controle de estoque
* fluxo de caixa básico

---

# **7. Estrutura de Banco de Dados – Núcleo Global**

Baseado no conjunto de scripts fornecidos e reorganizados:

### **7.1 Tabela `users`**

Gerenciamento global de identidade, integrando Clerk + Supabase.

### **7.2 Tabela `boteco`**

Cadastro fiscal, administrativo e referência para schemas privados.

### **7.3 Tabela `user_boteco`**

Associação usuários ↔ comércio, planos, acesso, validade.

---

# **8. Diferenciais Estratégicos**

### **8.1 Offline-first real**

A maioria dos concorrentes não oferece operação sem internet.

### **8.2 Low-cost & high-tech**

Tecnologia moderna e acessível, com UX superior.

### **8.3 Arquitetura multitenant de verdade**

Isolamento completo sem instâncias duplicadas.

### **8.4 Foco em inclusão**

Narrativa Monynha Softwares:

* acessibilidade
* democratização de tecnologia
* preço justo
* respeito à diversidade

### **8.5 Super App de Gestão**

O Boteco Pro não é só um “sistema de mesa e comanda”.
É um **ERP completo** para pequenos negócios.

---

# **9. Roadmap MVP → Série A**

### **Fase 1 – MVP Operacional**

* Onboarding + cadastro
* App operacional (mesas, pedidos, cozinha, caixa)
* Estoque básico
* Relatórios simples
* Painel administrativo

### **Fase 2 – Monetização & Billing**

* pagamentos recorrentes
* upgrade/downgrade
* trial + retenção

### **Fase 3 – Automação & IA**

* previsão de vendas
* otimização de cardápio
* sugestões automáticas de compra
* OCR para notas fiscais

### **Fase 4 – Marketplace**

* integração com delivery
* integrações financeiras
* fornecedores parceiros
* compra de insumos pelo app

---

# **10. Conclusão**

O **Boteco Pro** consolida-se como a plataforma moderna, acessível e poderosa para negócios do setor alimentício, preenchendo a lacuna deixada por softwares caros, difíceis de usar e tecnologicamente ultrapassados.

A combinação da arquitetura técnica sólida, propósito social da Monynha Softwares, foco em experiência do usuário e visão de longo prazo da plataforma colocam o Boteco Pro em posição privilegiada para escalar tanto no Brasil quanto no mercado internacional.

---
Em falta:

📄 **PDF empresarial**
🎨 **Pitch Deck**
📊 **Roadmap visual**
🧱 **Arquitetura detalhada de microserviços**
📝 **PRD completo (Product Requirements Document)**
📐 **Diagrama ER completo de todas as tabelas**

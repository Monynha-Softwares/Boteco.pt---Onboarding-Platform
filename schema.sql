CREATE TYPE stock_movement_type AS ENUM ('sale', 'production_in', 'manual_adjustment')

CREATE TABLE auth.users (
	instance_id UUID, 
	id UUID NOT NULL, 
	aud VARCHAR(255), 
	role VARCHAR(255), 
	email VARCHAR(255), 
	encrypted_password VARCHAR(255), 
	email_confirmed_at TIMESTAMP WITH TIME ZONE, 
	invited_at TIMESTAMP WITH TIME ZONE, 
	confirmation_token VARCHAR(255), 
	confirmation_sent_at TIMESTAMP WITH TIME ZONE, 
	recovery_token VARCHAR(255), 
	recovery_sent_at TIMESTAMP WITH TIME ZONE, 
	email_change_token_new VARCHAR(255), 
	email_change VARCHAR(255), 
	email_change_sent_at TIMESTAMP WITH TIME ZONE, 
	last_sign_in_at TIMESTAMP WITH TIME ZONE, 
	raw_app_meta_data JSONB, 
	raw_user_meta_data JSONB, 
	is_super_admin BOOLEAN, 
	created_at TIMESTAMP WITH TIME ZONE, 
	updated_at TIMESTAMP WITH TIME ZONE, 
	phone TEXT DEFAULT NULL::character varying, 
	phone_confirmed_at TIMESTAMP WITH TIME ZONE, 
	phone_change TEXT DEFAULT ''::character varying, 
	phone_change_token VARCHAR(255) DEFAULT ''::character varying, 
	phone_change_sent_at TIMESTAMP WITH TIME ZONE, 
	confirmed_at TIMESTAMP WITH TIME ZONE GENERATED ALWAYS AS (LEAST(email_confirmed_at, phone_confirmed_at)) STORED, 
	email_change_token_current VARCHAR(255) DEFAULT ''::character varying, 
	email_change_confirm_status SMALLINT DEFAULT 0, 
	banned_until TIMESTAMP WITH TIME ZONE, 
	reauthentication_token VARCHAR(255) DEFAULT ''::character varying, 
	reauthentication_sent_at TIMESTAMP WITH TIME ZONE, 
	is_sso_user BOOLEAN DEFAULT false NOT NULL, 
	deleted_at TIMESTAMP WITH TIME ZONE, 
	is_anonymous BOOLEAN DEFAULT false NOT NULL, 
	CONSTRAINT users_pkey PRIMARY KEY (id), 
	CONSTRAINT users_phone_key UNIQUE NULLS DISTINCT (phone), 
	CONSTRAINT users_email_change_confirm_status_check CHECK (email_change_confirm_status >= 0 AND email_change_confirm_status <= 2)
)


CREATE UNIQUE INDEX recovery_token_idx ON auth.users (recovery_token) WHERE ((recovery_token)::text !~ '^[0-9 ]*$'::text)
CREATE UNIQUE INDEX email_change_token_new_idx ON auth.users (email_change_token_new) WHERE ((email_change_token_new)::text !~ '^[0-9 ]*$'::text)
CREATE INDEX users_is_anonymous_idx ON auth.users (is_anonymous)
CREATE UNIQUE INDEX users_email_partial_key ON auth.users (email) WHERE (is_sso_user = false)
CREATE INDEX users_instance_id_email_idx ON auth.users (instance_id, lower(email::text))
CREATE UNIQUE INDEX reauthentication_token_idx ON auth.users (reauthentication_token) WHERE ((reauthentication_token)::text !~ '^[0-9 ]*$'::text)
CREATE UNIQUE INDEX email_change_token_current_idx ON auth.users (email_change_token_current) WHERE ((email_change_token_current)::text !~ '^[0-9 ]*$'::text)
CREATE UNIQUE INDEX confirmation_token_idx ON auth.users (confirmation_token) WHERE ((confirmation_token)::text !~ '^[0-9 ]*$'::text)
CREATE INDEX users_instance_id_idx ON auth.users (instance_id)
COMMENT ON TABLE auth.users IS 'Auth: Stores user login data within a secure schema.'
COMMENT ON COLUMN auth.users.is_sso_user IS 'Auth: Set this column to true when the account comes from SSO. These accounts can have duplicate emails.'

CREATE TABLE orders (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	table_id UUID, 
	customer_name TEXT, 
	status TEXT DEFAULT 'open'::text NOT NULL, 
	total NUMERIC(10, 2) DEFAULT 0 NOT NULL, 
	subtotal NUMERIC(10, 2) DEFAULT 0 NOT NULL, 
	discount NUMERIC(10, 2) DEFAULT 0, 
	tax NUMERIC(10, 2) DEFAULT 0, 
	payment_method TEXT, 
	payment_status TEXT DEFAULT 'pending'::text, 
	notes TEXT, 
	opened_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	closed_at TIMESTAMP WITH TIME ZONE, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT orders_pkey1 PRIMARY KEY (id), 
	CONSTRAINT orders_payment_method_check CHECK (payment_method = ANY (ARRAY['cash'::text, 'credit'::text, 'debit'::text, 'pix'::text, 'other'::text])), 
	CONSTRAINT orders_payment_status_check CHECK (payment_status = ANY (ARRAY['pending'::text, 'paid'::text, 'cancelled'::text])), 
	CONSTRAINT orders_status_check CHECK (status = ANY (ARRAY['open'::text, 'in_progress'::text, 'ready'::text, 'closed'::text, 'cancelled'::text]))
)


CREATE INDEX idx_orders_closed_at ON orders (closed_at)
CREATE INDEX idx_orders_table_id ON orders (table_id)
CREATE INDEX idx_orders_company_id ON orders (company_id)
CREATE INDEX idx_orders_status ON orders (status)
CREATE INDEX idx_orders_opened_at ON orders (opened_at)

CREATE TABLE tables (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	number INTEGER NOT NULL, 
	capacity INTEGER DEFAULT 4, 
	status TEXT DEFAULT 'available'::text NOT NULL, 
	current_order_id UUID, 
	location TEXT, 
	notes TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	name TEXT NOT NULL, 
	CONSTRAINT tables_pkey PRIMARY KEY (id), 
	CONSTRAINT tables_company_id_number_key UNIQUE NULLS DISTINCT (company_id, number), 
	CONSTRAINT tables_company_name_unique UNIQUE NULLS DISTINCT (company_id, name), 
	CONSTRAINT tables_status_check CHECK (status = ANY (ARRAY['available'::text, 'occupied'::text, 'reserved'::text, 'maintenance'::text]))
)


CREATE INDEX idx_tables_company_id ON tables (company_id)
CREATE INDEX idx_tables_status ON tables (status)
CREATE UNIQUE INDEX tables_company_id_number_idx ON tables (company_id, number)
CREATE INDEX idx_tables_current_order_id ON tables (current_order_id)
CREATE UNIQUE INDEX tables_company_id_name_idx ON tables (company_id, name)
COMMENT ON COLUMN tables.number IS 'Numeric table identifier. Used by mobile app for sorting/display.'
COMMENT ON COLUMN tables.name IS 'Human-readable table name (e.g., "Mesa 5", "VIP Table 1"). Must be unique within company.'

CREATE TABLE users (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	email TEXT NOT NULL, 
	username TEXT NOT NULL, 
	tax_number TEXT NOT NULL, 
	first_name TEXT NOT NULL, 
	last_name TEXT NOT NULL, 
	birth_date DATE NOT NULL, 
	country TEXT NOT NULL, 
	postal_code TEXT NOT NULL, 
	house_number TEXT NOT NULL, 
	associated_establishment_name TEXT, 
	establishment_tax_number TEXT, 
	is_owner BOOLEAN DEFAULT false NOT NULL, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
	CONSTRAINT users_pkey PRIMARY KEY (id), 
	CONSTRAINT users_email_key UNIQUE NULLS DISTINCT (email), 
	CONSTRAINT users_tax_number_key UNIQUE NULLS DISTINCT (tax_number), 
	CONSTRAINT users_username_key UNIQUE NULLS DISTINCT (username)
)



CREATE TABLE contact_requests (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	name TEXT NOT NULL, 
	email TEXT NOT NULL, 
	phone TEXT, 
	message TEXT NOT NULL, 
	channel TEXT DEFAULT 'web-form'::text NOT NULL, 
	status TEXT DEFAULT 'new'::text NOT NULL, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
	responded_at TIMESTAMP WITH TIME ZONE, 
	tags TEXT[], 
	estimated_value NUMERIC, 
	CONSTRAINT contact_requests_pkey PRIMARY KEY (id)
)



CREATE TABLE pg_stat_statements_info (
	dealloc BIGINT, 
	stats_reset TIMESTAMP WITH TIME ZONE
)



CREATE TABLE pg_stat_statements (
	userid OID, 
	dbid OID, 
	toplevel BOOLEAN, 
	queryid BIGINT, 
	query TEXT, 
	plans BIGINT, 
	total_plan_time DOUBLE PRECISION, 
	min_plan_time DOUBLE PRECISION, 
	max_plan_time DOUBLE PRECISION, 
	mean_plan_time DOUBLE PRECISION, 
	stddev_plan_time DOUBLE PRECISION, 
	calls BIGINT, 
	total_exec_time DOUBLE PRECISION, 
	min_exec_time DOUBLE PRECISION, 
	max_exec_time DOUBLE PRECISION, 
	mean_exec_time DOUBLE PRECISION, 
	stddev_exec_time DOUBLE PRECISION, 
	rows BIGINT, 
	shared_blks_hit BIGINT, 
	shared_blks_read BIGINT, 
	shared_blks_dirtied BIGINT, 
	shared_blks_written BIGINT, 
	local_blks_hit BIGINT, 
	local_blks_read BIGINT, 
	local_blks_dirtied BIGINT, 
	local_blks_written BIGINT, 
	temp_blks_read BIGINT, 
	temp_blks_written BIGINT, 
	shared_blk_read_time DOUBLE PRECISION, 
	shared_blk_write_time DOUBLE PRECISION, 
	local_blk_read_time DOUBLE PRECISION, 
	local_blk_write_time DOUBLE PRECISION, 
	temp_blk_read_time DOUBLE PRECISION, 
	temp_blk_write_time DOUBLE PRECISION, 
	wal_records BIGINT, 
	wal_fpi BIGINT, 
	wal_bytes NUMERIC, 
	jit_functions BIGINT, 
	jit_generation_time DOUBLE PRECISION, 
	jit_inlining_count BIGINT, 
	jit_inlining_time DOUBLE PRECISION, 
	jit_optimization_count BIGINT, 
	jit_optimization_time DOUBLE PRECISION, 
	jit_emission_count BIGINT, 
	jit_emission_time DOUBLE PRECISION, 
	jit_deform_count BIGINT, 
	jit_deform_time DOUBLE PRECISION, 
	stats_since TIMESTAMP WITH TIME ZONE, 
	minmax_stats_since TIMESTAMP WITH TIME ZONE
)



CREATE TABLE companies (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	name TEXT NOT NULL, 
	slug TEXT NOT NULL, 
	cnpj TEXT, 
	owner_id UUID NOT NULL, 
	plan_type TEXT DEFAULT 'free'::text NOT NULL, 
	realtime_enabled BOOLEAN DEFAULT false, 
	is_active BOOLEAN DEFAULT true, 
	logo_url TEXT, 
	phone TEXT, 
	email TEXT, 
	address TEXT, 
	city TEXT, 
	state TEXT, 
	country TEXT DEFAULT 'BR'::text, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT companies_pkey PRIMARY KEY (id), 
	CONSTRAINT companies_owner_id_fkey FOREIGN KEY(owner_id) REFERENCES auth.users (id) ON DELETE CASCADE, 
	CONSTRAINT companies_cnpj_key UNIQUE NULLS DISTINCT (cnpj), 
	CONSTRAINT companies_slug_key UNIQUE NULLS DISTINCT (slug), 
	CONSTRAINT companies_plan_type_check CHECK (plan_type = ANY (ARRAY['free'::text, 'basic'::text, 'premium'::text]))
)


CREATE INDEX idx_companies_owner_id ON companies (owner_id)
CREATE INDEX idx_companies_slug ON companies (slug)
CREATE INDEX idx_companies_is_active ON companies (is_active)

CREATE TABLE boteco (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	public_name TEXT NOT NULL, 
	username TEXT NOT NULL, 
	service_category TEXT NOT NULL, 
	offered_products_services TEXT, 
	average_staff_count INTEGER, 
	social_links JSONB, 
	has_own_digital_infra BOOLEAN DEFAULT false NOT NULL, 
	vibe_tags TEXT[], 
	establishment_tax_number TEXT, 
	country TEXT NOT NULL, 
	postal_code TEXT NOT NULL, 
	owner_tax_number TEXT NOT NULL, 
	reference TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
	created_by_email TEXT NOT NULL, 
	created_by_user_id UUID, 
	CONSTRAINT boteco_pkey PRIMARY KEY (id), 
	CONSTRAINT boteco_created_by_user_id_fkey FOREIGN KEY(created_by_user_id) REFERENCES users (id) ON DELETE SET NULL, 
	CONSTRAINT boteco_owner_tax_number_key UNIQUE NULLS DISTINCT (owner_tax_number), 
	CONSTRAINT boteco_username_key UNIQUE NULLS DISTINCT (username)
)


CREATE INDEX idx_boteco_created_by ON boteco (created_by_user_id)

CREATE TABLE profiles (
	id UUID NOT NULL, 
	username TEXT, 
	avatar_url TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	first_name TEXT, 
	last_name TEXT, 
	CONSTRAINT profiles_pkey PRIMARY KEY (id), 
	CONSTRAINT profiles_id_fkey FOREIGN KEY(id) REFERENCES auth.users (id) ON DELETE CASCADE, 
	CONSTRAINT profiles_username_key UNIQUE NULLS DISTINCT (username)
)


COMMENT ON TABLE profiles IS 'User profiles for BotecoPro app. Extends auth.users with app-specific fields.'

CREATE TABLE faturacoes (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	order_id UUID NOT NULL, 
	company_id UUID NOT NULL, 
	table_id UUID, 
	total NUMERIC NOT NULL, 
	payment_method TEXT, 
	payment_status TEXT, 
	notes TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT faturacoes_pkey PRIMARY KEY (id), 
	CONSTRAINT faturacoes_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id), 
	CONSTRAINT faturacoes_order_id_fkey FOREIGN KEY(order_id) REFERENCES orders (id) ON DELETE CASCADE, 
	CONSTRAINT faturacoes_table_id_fkey FOREIGN KEY(table_id) REFERENCES tables (id)
)


CREATE INDEX idx_faturacoes_company_id ON faturacoes (company_id)

CREATE TABLE company_settings (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	realtime_enabled BOOLEAN DEFAULT false, 
	currency TEXT DEFAULT 'BRL'::text, 
	timezone TEXT DEFAULT 'America/Sao_Paulo'::text, 
	language TEXT DEFAULT 'pt_BR'::text, 
	tax_rate NUMERIC(5, 2) DEFAULT 0, 
	service_fee NUMERIC(5, 2) DEFAULT 0, 
	receipt_footer TEXT, 
	notifications_enabled BOOLEAN DEFAULT true, 
	auto_print_orders BOOLEAN DEFAULT false, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT company_settings_pkey PRIMARY KEY (id), 
	CONSTRAINT company_settings_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE, 
	CONSTRAINT company_settings_company_id_key UNIQUE NULLS DISTINCT (company_id)
)


CREATE INDEX idx_company_settings_company_id ON company_settings (company_id)

CREATE TABLE sales (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	order_id UUID NOT NULL, 
	total NUMERIC(10, 2) NOT NULL, 
	subtotal NUMERIC(10, 2) NOT NULL, 
	discount NUMERIC(10, 2) DEFAULT 0, 
	tax NUMERIC(10, 2) DEFAULT 0, 
	payment_method TEXT NOT NULL, 
	sale_date TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
	cashier_id UUID, 
	notes TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT sales_pkey1 PRIMARY KEY (id), 
	CONSTRAINT sales_cashier_id_fkey FOREIGN KEY(cashier_id) REFERENCES auth.users (id), 
	CONSTRAINT sales_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE, 
	CONSTRAINT sales_order_id_fkey1 FOREIGN KEY(order_id) REFERENCES orders (id) ON DELETE RESTRICT, 
	CONSTRAINT sales_payment_method_check CHECK (payment_method = ANY (ARRAY['cash'::text, 'credit'::text, 'debit'::text, 'pix'::text, 'other'::text]))
)


CREATE INDEX idx_sales_order_id ON sales (order_id)
CREATE INDEX idx_sales_cashier_id ON sales (cashier_id)
CREATE INDEX idx_sales_sale_date ON sales (sale_date)
CREATE INDEX idx_sales_company_id ON sales (company_id)
CREATE INDEX idx_sales_payment_method ON sales (payment_method)

CREATE TABLE products (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	price NUMERIC(10, 2) DEFAULT 0 NOT NULL, 
	cost NUMERIC(10, 2) DEFAULT 0, 
	stock NUMERIC(10, 3) DEFAULT 0 NOT NULL, 
	min_stock NUMERIC(10, 3) DEFAULT 0, 
	category TEXT NOT NULL, 
	unit TEXT NOT NULL, 
	barcode TEXT, 
	image_url TEXT, 
	is_active BOOLEAN DEFAULT true, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	internal_notes TEXT, 
	CONSTRAINT products_pkey1 PRIMARY KEY (id), 
	CONSTRAINT products_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE, 
	CONSTRAINT products_category_check CHECK (category = ANY (ARRAY['drink'::text, 'food'::text, 'ingredient'::text, 'other'::text])), 
	CONSTRAINT products_unit_check CHECK (unit = ANY (ARRAY['un'::text, 'kg'::text, 'l'::text, 'ml'::text, 'g'::text]))
)


CREATE INDEX idx_products_is_active ON products (is_active)
CREATE INDEX idx_products_category ON products (category)
CREATE INDEX idx_products_stock ON products (stock)
CREATE INDEX idx_products_company_id ON products (company_id)
COMMENT ON COLUMN products.internal_notes IS 'Notas internas para controle do produto (não visíveis para clientes)'

CREATE TABLE company_users (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	user_id UUID NOT NULL, 
	role TEXT DEFAULT 'waiter'::text NOT NULL, 
	is_active BOOLEAN DEFAULT true, 
	invited_by UUID, 
	invited_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	accepted_at TIMESTAMP WITH TIME ZONE, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT company_users_pkey PRIMARY KEY (id), 
	CONSTRAINT company_users_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE, 
	CONSTRAINT company_users_invited_by_fkey FOREIGN KEY(invited_by) REFERENCES auth.users (id), 
	CONSTRAINT company_users_user_id_fkey FOREIGN KEY(user_id) REFERENCES auth.users (id) ON DELETE CASCADE, 
	CONSTRAINT company_users_company_id_user_id_key UNIQUE NULLS DISTINCT (company_id, user_id), 
	CONSTRAINT company_users_role_check CHECK (role = ANY (ARRAY['owner'::text, 'admin'::text, 'manager'::text, 'waiter'::text, 'cashier'::text, 'kitchen'::text]))
)


CREATE INDEX company_users_user_company_idx ON company_users (user_id, company_id)
CREATE INDEX idx_company_users_user_id ON company_users (user_id)
CREATE INDEX idx_company_users_user_company ON company_users (user_id, company_id)
CREATE INDEX idx_company_users_role ON company_users (role)
CREATE INDEX idx_company_users_company_id ON company_users (company_id)
CREATE INDEX idx_company_users_invited_by ON company_users (invited_by)

CREATE TABLE user_boteco (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	user_id UUID NOT NULL, 
	boteco_id UUID NOT NULL, 
	assigned_role TEXT DEFAULT 'owner'::text NOT NULL, 
	assigned_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
	reference TEXT, 
	plan TEXT NOT NULL, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
	CONSTRAINT user_boteco_pkey PRIMARY KEY (id), 
	CONSTRAINT user_boteco_boteco_id_fkey FOREIGN KEY(boteco_id) REFERENCES boteco (id) ON DELETE CASCADE, 
	CONSTRAINT user_boteco_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE, 
	CONSTRAINT user_boteco_plan_check CHECK (plan = ANY (ARRAY['boteco'::text, 'boteco_pro'::text, 'boteco_patrao'::text, 'boteco_babadeiro'::text]))
)


CREATE INDEX idx_user_boteco_boteco_id ON user_boteco (boteco_id)
CREATE INDEX idx_user_boteco_user_id ON user_boteco (user_id)

CREATE TABLE suppliers (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	name TEXT NOT NULL, 
	contact TEXT, 
	phone TEXT, 
	email TEXT, 
	cnpj TEXT, 
	address TEXT, 
	city TEXT, 
	state TEXT, 
	country TEXT DEFAULT 'BR'::text, 
	notes TEXT, 
	is_active BOOLEAN DEFAULT true, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT suppliers_pkey1 PRIMARY KEY (id), 
	CONSTRAINT suppliers_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE
)


CREATE INDEX idx_suppliers_company_id ON suppliers (company_id)
CREATE INDEX idx_suppliers_is_active ON suppliers (is_active)

CREATE TABLE reservations (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	table_id UUID, 
	customer_name TEXT NOT NULL, 
	customer_phone TEXT, 
	customer_email TEXT, 
	party_size INTEGER NOT NULL, 
	reservation_date TIMESTAMP WITH TIME ZONE NOT NULL, 
	status TEXT DEFAULT 'pending'::text NOT NULL, 
	notes TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT reservations_pkey PRIMARY KEY (id), 
	CONSTRAINT reservations_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE, 
	CONSTRAINT reservations_table_id_fkey FOREIGN KEY(table_id) REFERENCES tables (id) ON DELETE SET NULL, 
	CONSTRAINT reservations_status_check CHECK (status = ANY (ARRAY['pending'::text, 'confirmed'::text, 'arrived'::text, 'cancelled'::text, 'no_show'::text]))
)


CREATE INDEX idx_reservations_company_id ON reservations (company_id)
CREATE INDEX idx_reservations_reservation_date ON reservations (reservation_date)
CREATE INDEX idx_reservations_table_id ON reservations (table_id)

CREATE TABLE stock_movements (
	id BIGSERIAL NOT NULL, 
	product_id UUID NOT NULL, 
	movement_type stock_movement_type NOT NULL, 
	quantity NUMERIC(12, 3) NOT NULL, 
	related_order_id UUID, 
	related_production_id UUID, 
	reason TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
	company_id UUID NOT NULL, 
	CONSTRAINT stock_movements_pkey PRIMARY KEY (id), 
	CONSTRAINT stock_movements_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE
)


CREATE INDEX stock_movements_company_created_idx ON stock_movements (company_id, created_at)
CREATE INDEX stock_movements_company_id_idx ON stock_movements (company_id)

CREATE TABLE recipes (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	product_id UUID NOT NULL, 
	name TEXT NOT NULL, 
	yield_quantity NUMERIC(10, 3) DEFAULT 1 NOT NULL, 
	yield_unit TEXT NOT NULL, 
	preparation_time INTEGER, 
	instructions TEXT, 
	notes TEXT, 
	is_active BOOLEAN DEFAULT true, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT recipes_pkey1 PRIMARY KEY (id), 
	CONSTRAINT recipes_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE, 
	CONSTRAINT recipes_product_id_fkey1 FOREIGN KEY(product_id) REFERENCES products (id) ON DELETE CASCADE, 
	CONSTRAINT recipes_yield_unit_check CHECK (yield_unit = ANY (ARRAY['un'::text, 'kg'::text, 'l'::text, 'ml'::text, 'g'::text]))
)


CREATE INDEX idx_recipes_is_active ON recipes (is_active)
CREATE INDEX idx_recipes_product_id ON recipes (product_id)
CREATE INDEX idx_recipes_company_id ON recipes (company_id)

CREATE TABLE order_items (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	order_id UUID NOT NULL, 
	product_id UUID NOT NULL, 
	quantity NUMERIC(10, 3) DEFAULT 1 NOT NULL, 
	unit_price NUMERIC(10, 2) NOT NULL, 
	subtotal NUMERIC(10, 2) NOT NULL, 
	notes TEXT, 
	status TEXT DEFAULT 'pending'::text, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT order_items_pkey1 PRIMARY KEY (id), 
	CONSTRAINT order_items_order_id_fkey1 FOREIGN KEY(order_id) REFERENCES orders (id) ON DELETE CASCADE, 
	CONSTRAINT order_items_product_id_fkey1 FOREIGN KEY(product_id) REFERENCES products (id) ON DELETE RESTRICT, 
	CONSTRAINT order_items_status_check CHECK (status = ANY (ARRAY['pending'::text, 'preparing'::text, 'ready'::text, 'delivered'::text, 'cancelled'::text]))
)


CREATE INDEX idx_order_items_status ON order_items (status)
CREATE INDEX idx_order_items_order_id ON order_items (order_id)
CREATE INDEX idx_order_items_product_id ON order_items (product_id)

CREATE TABLE internal_productions (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	company_id UUID NOT NULL, 
	product_id UUID NOT NULL, 
	recipe_id UUID, 
	quantity NUMERIC(10, 3) NOT NULL, 
	date DATE DEFAULT CURRENT_DATE NOT NULL, 
	status TEXT DEFAULT 'planned'::text NOT NULL, 
	cost NUMERIC(10, 2) DEFAULT 0, 
	notes TEXT, 
	completed_at TIMESTAMP WITH TIME ZONE, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT internal_productions_pkey PRIMARY KEY (id), 
	CONSTRAINT internal_productions_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE, 
	CONSTRAINT internal_productions_product_id_fkey FOREIGN KEY(product_id) REFERENCES products (id) ON DELETE RESTRICT, 
	CONSTRAINT internal_productions_recipe_id_fkey FOREIGN KEY(recipe_id) REFERENCES recipes (id) ON DELETE SET NULL, 
	CONSTRAINT internal_productions_status_check CHECK (status = ANY (ARRAY['planned'::text, 'in_progress'::text, 'completed'::text, 'cancelled'::text]))
)


CREATE INDEX idx_internal_productions_product_id ON internal_productions (product_id)
CREATE INDEX idx_internal_productions_status ON internal_productions (status)
CREATE INDEX idx_internal_productions_company_id ON internal_productions (company_id)
CREATE INDEX idx_internal_productions_recipe_id ON internal_productions (recipe_id)
CREATE INDEX idx_internal_productions_date ON internal_productions (date)

CREATE TABLE recipe_ingredients (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	recipe_id UUID NOT NULL, 
	product_id UUID NOT NULL, 
	quantity NUMERIC(10, 3) NOT NULL, 
	unit TEXT NOT NULL, 
	notes TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT recipe_ingredients_pkey1 PRIMARY KEY (id), 
	CONSTRAINT recipe_ingredients_product_id_fkey FOREIGN KEY(product_id) REFERENCES products (id) ON DELETE RESTRICT, 
	CONSTRAINT recipe_ingredients_recipe_id_fkey1 FOREIGN KEY(recipe_id) REFERENCES recipes (id) ON DELETE CASCADE, 
	CONSTRAINT recipe_ingredients_unit_check CHECK (unit = ANY (ARRAY['un'::text, 'kg'::text, 'l'::text, 'ml'::text, 'g'::text]))
)


CREATE INDEX idx_recipe_ingredients_recipe_id ON recipe_ingredients (recipe_id)
CREATE INDEX idx_recipe_ingredients_product_id ON recipe_ingredients (product_id)

CREATE TABLE production_ingredients (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	production_id UUID NOT NULL, 
	product_id UUID NOT NULL, 
	quantity NUMERIC(10, 3) NOT NULL, 
	unit TEXT NOT NULL, 
	cost NUMERIC(10, 2) DEFAULT 0, 
	notes TEXT, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	CONSTRAINT production_ingredients_pkey1 PRIMARY KEY (id), 
	CONSTRAINT production_ingredients_product_id_fkey FOREIGN KEY(product_id) REFERENCES products (id) ON DELETE RESTRICT, 
	CONSTRAINT production_ingredients_production_id_fkey1 FOREIGN KEY(production_id) REFERENCES internal_productions (id) ON DELETE CASCADE, 
	CONSTRAINT production_ingredients_unit_check CHECK (unit = ANY (ARRAY['un'::text, 'kg'::text, 'l'::text, 'ml'::text, 'g'::text]))
)


CREATE INDEX idx_production_ingredients_production_id ON production_ingredients (production_id)
CREATE INDEX idx_production_ingredients_product_id ON production_ingredients (product_id)
ALTER TABLE tables ADD CONSTRAINT tables_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE
ALTER TABLE orders ADD CONSTRAINT orders_table_id_fkey1 FOREIGN KEY(table_id) REFERENCES tables (id) ON DELETE SET NULL
ALTER TABLE orders ADD CONSTRAINT orders_company_id_fkey FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE CASCADE
ALTER TABLE tables ADD CONSTRAINT fk_tables_current_order FOREIGN KEY(current_order_id) REFERENCES orders (id) ON DELETE SET NULL
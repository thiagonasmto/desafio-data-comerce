import { useState } from "react";
import './Dashboard.css';

export default function Dashboard() {
    const [isLoading, setIsLoading] = useState(false);

    const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        setIsLoading(true);

        try {
            const response = await fetch("http://localhost:8000/upload-csv/", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            if (response.ok) {
                alert(data.message);
            } else {
                alert(`Erro: ${data.error}`);
            }
        } catch (error) {
            alert("Erro ao enviar arquivo: " + error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="dash-container">
            <div className="sidebar">
                <h2 className="sidebar-title">Dashboard de Produtos</h2>

                {/* Upload de Arquivo */}
                <div className="sidebar-section">
                    <label htmlFor="file-upload" className="upload-label">Carregar Arquivo</label>
                    <input
                        type="file"
                        id="file-upload"
                        onChange={handleFileUpload}
                        className="upload-input"
                    />
                    {isLoading && <p className="loading-indicator">Carregando...</p>}
                </div>

                {/* Filtros */}
                <div className="sidebar-section">
                    <h3>Filtros</h3>
                    <select className="filter-select" name="year" id="year">
                        <option value="2020">2020</option>
                        <option value="2021">2021</option>
                    </select>
                    <select className="filter-select" name="state" id="state">
                        <option value="AC">Acre</option>
                        <option value="AL">Alagoas</option>
                        <option value="AP">Amapá</option>
                        <option value="AM">Amazonas</option>
                        <option value="BA">Bahia</option>
                        <option value="CE">Ceará</option>
                        <option value="DF">Distrito Federal</option>
                        <option value="ES">Espírito Santo</option>
                        <option value="GO">Goiás</option>
                        <option value="MA">Maranhão</option>
                        <option value="MT">Mato Grosso</option>
                        <option value="MS">Mato Grosso do Sul</option>
                        <option value="MG">Minas Gerais</option>
                        <option value="PA">Pará</option>
                        <option value="PB">Paraíba</option>
                        <option value="PR">Paraná</option>
                        <option value="PE">Pernambuco</option>
                        <option value="PI">Piauí</option>
                        <option value="RJ">Rio de Janeiro</option>
                        <option value="RN">Rio Grande do Norte</option>
                        <option value="RS">Rio Grande do Sul</option>
                        <option value="RO">Rondônia</option>
                        <option value="RR">Roraima</option>
                        <option value="SC">Santa Catarina</option>
                        <option value="SP">São Paulo</option>
                        <option value="SE">Sergipe</option>
                        <option value="TO">Tocantins</option>
                    </select>
                </div>

                {/* Botões para gráficos */}
                <div className="sidebar-section">
                    <button
                        className="btn"
                        onClick={async () => {
                            setIsLoading(true);
                            try {
                                const response = await fetch("http://localhost:8000/top-3-exportados/");
                                const data = await response.json();
                                if (response.ok) {
                                    alert(data.message);
                                } else {
                                    alert(`Erro: ${data.error}`);
                                }
                            } catch (error) {
                                alert("Erro ao gerar gráfico: " + error);
                            } finally {
                                setIsLoading(false);
                            }
                        }}
                    >
                        Top 3 Exportados
                    </button>
                    <button className="btn" onClick={() => console.log("Importados")}>
                        Top 3 Importados
                    </button>
                    <button className="btn" onClick={() => console.log("Exportados por mês")}>
                        Top 3 Exportados por Mês
                    </button>
                </div>
            </div>

            {/* Conteúdo principal */}
            <main className="main-content">
                <h1>Bem-vindo ao dashboard!</h1>
                <p>Selecione filtros e visualize os dados.</p>
            </main>
        </div>
    );
}

import logopic from './images/motherfucking-game.png'
import LoginModal from './modal';

export default function Header() {
    return (
        <nav className="navbar navbar-expand-md nav-underline md-body-tertiary">
            <LoginModal id = "Modal"/>
            <div className="navbar-brand">
                <a href="#">
                    <img src={logopic} alt="Logo" width="150" height="150"  style={{marginLeft: "1em"}} className="d-inline-block margin-right-md"/>
                </a>
            </div>
            <h1 className="navbar">Orange Cat Decks</h1>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div style={{width: "50%"}}/>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav me-auto mb-2 mb-lg-0 align-content-end">
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">Link</a>
                    </li>
                    <li className="nav-item dropdown">
                        <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Dropdown
                        </a>
                        <ul className="dropdown-menu">
                            <li><a className="dropdown-item" href="#">Action</a></li>
                            <li><a className="dropdown-item" href="#">Another action</a></li>
                            <li><hr className="dropdown-divider"/></li>
                            <li><a className="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                    <li className="nav-item">
                        <button className="nav-link" aria-disabled="true" data-bs-toggle="modal" data-bs-target="#Modal">Login</button>
                    </li>
                </ul>
                <form className="d-flex" style={{width: "25em", marginRight: "2.5em"}} role="search">
                    <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
                    <button className="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </nav>
    );
}